"""Build the sentence review from the author's Chapter One Markdown."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parents[1] / 'data'


def build():
    path = HERE.parent / 'chapters' / 'chapter-01-cove.md'
    raw = path.read_bytes()
    source = raw.decode('utf-8')
    spans = []
    # Reviewed quote uses for this source: quotation is not automatically speech.
    for m in re.finditer(r'"[^"\n]*"', source):
        content = m[0]
        kind = ('Imagined creator wording' if content == '"make him mean it."'
                else 'On-screen text' if content == '"Saving progress"'
                else 'Quoted description, not dialogue' if content == '"inspect character model."'
                else 'Spoken dialogue')
        spans.append((m.start(), m.end(), kind))
    extras = [('*Nah, man, go away. You\'ll slow us down.*', 'Remembered speech — friend quoting himself'),
              ('*Go on now, shoo.*', 'Imagined speech — Cove considers saying it'),
              ('*Go on now, shoo*', 'Rehearsed speech — Cove repeats it in his head'),
              ('*come on come on come on—*', 'Spoken dialogue — whispered'),
              ('*Should I take the apple to the horse?*', 'Inner monologue — direct thought')]
    for phrase, kind in extras:
        assert source.count(phrase) == 1, phrase
        start = source.index(phrase)
        spans.append((start, start + len(phrase), kind))
    for m in re.finditer(r'\*Saving progress\.?\*', source):
        kind = 'On-screen text' if m[0].endswith('.*') else 'Recalled on-screen text'
        spans.append((m.start(), m.end(), kind))
    sentences = []
    paragraphs = []
    for block in re.finditer(r'\S.*?(?=\n[ \t]*\n|\Z)', source, re.S):
        if block[0].startswith('#'):
            continue
        pid = len(paragraphs) + 1
        text = block[0].rstrip()
        # Full stops/questions/exclamations finish units. Ellipses within a
        # sentence do not. Interrupted spoken lines finish at their closing quote.
        ends = []
        for m in re.finditer(r'[.!?]["”*]*|…["”]|—["”*]', text):
            end = m.end()
            if end == len(text) or text[end].isspace():
                ends.append(end)
        if not ends or ends[-1] != len(text):
            ends.append(len(text))
        start = 0
        members = []
        for end in ends:
            while start < end and text[start].isspace():
                start += 1
            if start == end:
                continue
            a, b = block.start() + start, block.start() + end
            uses = [{'text': source[max(a,x):min(b,y)], 'kind': kind,
                     'char_start': max(a,x), 'char_end': min(b,y)}
                    for x,y,kind in spans if x < b and y > a]
            if uses:
                label = ' / '.join(dict.fromkeys(u['kind'] for u in uses))
                covered = sum(u['char_end']-u['char_start'] for u in uses)
                if source[a:b].strip(' *"') and covered < len(source[a:b].strip()):
                    label += ' + narration/inner monologue'
            else:
                label = 'Narration / inner monologue'
            sid = f'S{len(sentences)+1:03d}'
            sentences.append({'id': sid, 'paragraph': pid, 'text': source[a:b],
                              'label': label, 'quoted_uses': uses,
                              'char_start': a, 'char_end': b,
                              'source_line': source.count('\n', 0, a)+1,
                              'character_states': []})
            members.append(sid)
            start = end
        paragraphs.append({'number': pid, 'char_start': block.start(),
                           'char_end': block.end(), 'sentences': members})

    notes = json.loads((HERE / 'state-notes.json').read_text())
    for note in notes:
        evidence = []
        for quote in note['quotes']:
            assert source.count(quote) == 1, ('Evidence must identify one occurrence', quote)
            start = source.index(quote)
            end = start + len(quote)
            ids = [s['id'] for s in sentences if s['char_start'] < end and s['char_end'] > start]
            assert ids, quote
            evidence.append({'quote': quote, 'sentence_ids': ids})
        ids = list(dict.fromkeys(sid for e in evidence for sid in e['sentence_ids']))
        record = dict(note, evidence=evidence, sentence_ids=ids, character='Cove')
        sentences[int(ids[0][1:])-1]['character_states'].append(record)

    # Every non-whitespace story character appears in exactly one source unit.
    coverage = [0] * len(source)
    for s in sentences:
        assert source[s['char_start']:s['char_end']] == s['text']
        for i in range(s['char_start'], s['char_end']):
            coverage[i] += 1
    for p in paragraphs:
        assert all(coverage[i] == 1 for i in range(p['char_start'], p['char_end']) if not source[i].isspace())
    assert max(coverage) == 1
    assert path.read_bytes() == raw
    output = {'source': '../chapters/chapter-01-cove.md', 'sha256': hashlib.sha256(raw).hexdigest(),
              'segmentation_policy': 'Punctuation-delimited sentences and intentional fragments. Dialogue tags stay with their sentence. Internal ellipses stay within a unit. IDs describe this fixed source version.',
              'note': 'Labels and character-state descriptions are a first editorial reading, not author-approved ground truth. An empty state list does not prove a sentence has no character significance.',
              'paragraphs': paragraphs, 'sentences': sentences}
    (HERE / 'sentences.json').write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n')
    intro = f'''# Chapter One — Sentence-by-sentence character states

Source: [your Chapter One Markdown](../chapters/chapter-01-cove.md), unchanged.

**{len(sentences)} source units; {len(notes)} character-state notes.** Read in chapter order below. Each sentence has a simple source ID. Short intentional fragments such as “Same boots.” also get IDs; they are retained rather than silently merged or discarded.

Words inside backticks are exact source text, including original Markdown emphasis. Dialogue tags remain with their sentence. Sentences containing both dialogue and narration are labeled accordingly. A remembered line, a hypothetical line, and actual speech are distinguished using context.

Character-state notes are a reading grounded in the cited sentences. “Explicit” means the wording is present in the chapter, not that Cove's account is objectively true or fully sincere. “Explicit self-presentation” marks a claim Cove makes about himself or others whose performance or sincerity matters. “Interpretation” marks an inference. “Read together” points to tension across passages. “Cove's later reading” records his subsequent response to these notes; it is additional character testimony, not a replacement for the chapter. Sentences without notes remain present; absence of a note is not a claim that nothing matters there. Neighboring sentence references provide context.

The simple IDs are tied to this source version. If the chapter is edited, reconcile the IDs before attaching further data. Technical source offsets are saved in `sentences.json`; you do not need them to read this document. No graph or embeddings are generated here.

'''
    lines = [intro]
    for p in paragraphs:
        lines.append(f'## Passage {p["number"]}\n\n')
        for sid in p['sentences']:
            s = sentences[int(sid[1:])-1]
            lines.append(f'### {sid} — {s["label"]}\n\n')
            lines.append('`' + s['text'].replace('\n', '`\n\n`') + '`\n\n')
            for n in s['character_states']:
                lines.append(f'**Character state — {n["basis"]}:** {n["state"]}\n\n')
                lines.append('**Supported by:** ' + ', '.join(n['sentence_ids']) + '.\n\n')
                if n.get('context'):
                    lines.append(n['context']+'\n\n')
                if n.get('tension'):
                    lines.append('**Read together:** '+n['tension']+'\n\n')
                if n.get('cove_reading'):
                    lines.append('**Cove’s later reading:** '+n['cove_reading']+'\n\n')
    (HERE / 'chapter-01-sentence-review.md').write_text(''.join(lines))
    print(f'{len(sentences)} source units; {len(paragraphs)} passages; {len(notes)} grounded state notes. Exact-source coverage passed.')


if __name__ == '__main__':
    build()
