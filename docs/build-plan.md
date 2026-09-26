# Build plan: Cove’s character states, reference, and continuity

## Purpose and scope

Build a granular map of Chapter One using philosophy of mind: what Cove perceives, represents, believes, imagines, feels, considers, and does; what each state is about; and how events and states relate through the story. Treat the character as a process of events and relationships.

The initial corpus is one chapter, currently divided into 672 sentences and intentional fragments, with 103 character-state notes. Those notes are a starting interpretation, not a complete inventory. Further extraction must reach the granularity demonstrated below without requiring the author to identify each missing state.

The implementation will use Python and PyTorch to make this representation inspectable and computable. Its initial purpose is mapping and analysis. Future-state prediction, comparing Cove with other characters, and training a dialogue model are outside this build’s scope.

All extracted states are called **character states**. Philosophy-of-mind terms describe their kinds and relations. We study experience as depicted in the fiction; the map itself does not establish consciousness in a model.

## Implementation milestones

### 1. Annotate the apple sequence at the required granularity

Extend the existing data format and renderer for entities, events, character states, represented content, and evidence-backed relations. Annotate S282–S383, including the intervening resistance and attribution rather than compressing the six-step example into six exhaustive states.

**Deliverable:** the existing sentence review displays exact text, granular states, their targets, and connections in readable language. A reader can distinguish thinking of the mare from thinking about that thought.

**Done when:** each step and distinction in the apple sequence can be traced to the source; decision and causation inferences are labeled; original source text is unchanged; the existing notes and Cove readings are retained or explicitly refined.

### 2. Apply the rules to the entire chapter

Review all source units with the same procedure. Resolve references and preserve separate belief occurrences across time. Use the opening narration, moving-sun passage, and imagined-lunch passage as checks that the procedure generalizes beyond the apple. Inspect language such as “I know,” “maybe,” “should,” “like,” and “as if” in context.

**Deliverable:** a complete granular annotation in the existing data and review files, including reasons for units with no standalone state.

**Done when:** every unit has a review status; all referenced objects/states resolve or carry explicit ambiguity; there are no unsupported assertions that metaphor is literal or imagined events occurred.

### 3. Build an inspectable graph from the annotations

Generate nodes and typed relations directly from the reviewed data. Start with Python dictionaries and lists; a separate graph database is unnecessary for this chapter. Provide a focused map for a selected passage and a readable trace back to each supporting sentence. Avoid a single unreadable diagram of the whole chapter.

**Deliverable:** one source-linked character map, with views for plot events, representational targets, higher-order reflection, and continuity. These are views of the same data.

**Done when:** queries can show the apple’s changing relevance, the thought targeted by S309, the deliberation targeted by S322–S328, and the alternatives still open when Cove imagines lunch. Filtering out inferred causal links must leave chronology intact.

### 4. Implement NLP analysis of Cove’s language

NLP is a required part of the build. Analyze how Cove uses language throughout this chapter and connect the findings to the character states, representational targets, and plot relations from milestones 1–3.

Implement a reproducible local pipeline with tokenization, lemmatization, part-of-speech tagging, and dependency parsing. Preserve the existing sentence IDs and exact source offsets: a parser’s sentence boundaries must not silently replace the project’s source units. Treat markup as formatting while retaining a mapping to the original Markdown. Record the chosen parser and model versions when the environment is set up.

Analyze these features:

- **Vocabulary and repetition:** word and lemma frequencies, repeated phrases, and vocabulary by passage. Inspect terms concerning generation, agency, obligation, and care. Show occurrences and passage lengths alongside counts so a longer passage is not mistaken for a stronger tendency.
- **Reference:** entity mentions, pronouns, and candidate referents. Resolve “it” in the apple passage using context; distinguish an object reference from reference to a thought or proposition. Preserve ambiguous candidates rather than forcing a match.
- **Predicates and agency:** who perceives, thinks, acts, or is acted upon; grammatical subjects and objects; first-person versus creator-attributed action. Link grammatical analysis to the existing event and state records for inspection.
- **Modality and negation:** “should,” “could,” “maybe,” “not,” and their scope. Distinguish considering an action, asserting an action, denying a state, and expressing uncertainty. The “should I” sequence is a required example.
- **Syntax and inner narration:** questions, fragments, tense/aspect, repeated self-reference, and reported or quoted speech. Examine how these appear during perception, higher-order reflection, deliberation, and action.
- **Metaphor, irony, and self-presentation:** locate and annotate expressions such as the apple’s gaze, the porch-light comparison, and “not rooting for them, exactly.” Use parser output as evidence about language structure; the figurative and pragmatic readings remain supported interpretations linked to the text and Cove’s existing feedback.
- **Change through the chapter:** inspect how these features vary across passages and align with the mapped state changes. This is analysis of the written chapter, not a prediction task or a comparison with another character.

Connect token/span features to sentence IDs and from there to the character map. Reuse the same entity identities and source spans. Define the selected numeric language features, their vocabulary, and how missing values will be represented. Milestone 5 converts these features into PyTorch tensors alongside the state and relation tensors.

**Deliverable:** an NLP pipeline and language-analysis view in the current generated review. It must show words and constructions in context, links to their mapped states, and summaries of how their use changes across the chapter. Annotation assistance may be an additional benefit, but it is not the milestone’s sole purpose.

**Done when:** all chapter text is processed with source offsets preserved; counts are reproducible; manually checked examples verify reference candidates, negation scope, and modality; the apple, opening, sun, and lunch passages can be inspected through both their linguistic features and character-state map. Metaphor is not promoted to a literal event, and grammatical structure is not treated as proof of a psychological or causal relation.

### 5. Implement the map and language features in PyTorch

Create a project environment and record a compatible PyTorch dependency. Start on CPU; this chapter does not require a GPU for the proposed tensor operations.

Translate categorical node attributes and the NLP features defined in milestone 4 into documented feature tensors, and typed links into integer endpoint tensors. Use separate masks for known, unknown, explicit, and inferred values; do not encode unknown as false. Keep a reversible lookup from every tensor row and relation back to its readable record and source sentences. PyTorch supports [multidimensional tensors](https://docs.pytorch.org/docs/stable/tensors) and [sparse coordinate tensors](https://docs.pytorch.org/docs/2.14/generated/torch.sparse_coo_tensor.html), which can represent selected relation matrices when useful.

Implement these concrete operations:

- Select perceptual states about currently present objects versus thoughts about absent objects.
- Follow `reflects_on` links to show a higher-order state and the state it concerns.
- Select a passage interval and inspect which entities recur while their attributed states change.
- Trace only evidence-backed causal links, keeping reasons, associations, and sequence available as different relation types.
- Decode every result into readable labels and source sentences in the existing review or a terminal response.

**Deliverable:** a runnable PyTorch representation and query module. This is real tensor computation over the chapter’s annotated structure. No learned weights are required for this milestone; a tensor encoding itself does not learn or establish meaning.

**Done when:** tensor queries return the same source-linked results as straightforward Python queries on the reviewed annotations, including mixed explicit/inferred and unknown cases. Empty relations and repeated references must be handled correctly.

## Required granularity: the apple sequence

Sentence references point to the current [sentence review](../data/chapter-01-sentence-review.md), generated from [Chapter One](../chapters/chapter-01-cove.md).

1. **He looks at the apple: perception**, directed at the apple present in the scene. S282–S283.
2. **The mare comes to mind: representation of an absent object**, directed at the mare; how he knows about her is unspecified. S303.
3. **He asks why he is thinking about a horse: higher-order reflection**, directed at his own mare-thought. S309 targets S303.
4. **He considers taking her the apple: deliberation about a possible action.** S316.
5. **He notices that he is asking “should I”: reflection on his own deliberation.** S322–S328 target the deliberation in S316.
6. **He chooses to walk it over: decision**, followed by action. S370–S371: the action is explicit; the decision is inferred from the choice context.

These six steps establish the required detail, not an exhaustive inventory. Capture intervening appraisals, resistance, alternatives, and attribution too. Perception also involves representation; higher-order reflection specifically targets another character state. These working distinctions draw on [representational theories](https://plato.stanford.edu/entries/consciousness-representational/) and [higher-order theories](https://plato.stanford.edu/entries/consciousness-higher/).

## Core modeling rules

- **Granularity throughout:** inspect every meaningful clause, including opening self-descriptions and reflection with no external trigger. Separate distinct states within a sentence; combine evidence across sentences when needed. Mark every source unit reviewed, with a reason when it supports no separate state.
- **Narrative frame and time:** treat Cove’s narration as ongoing present inner narration, with no assumed external listener. Distinguish explicit speech. Separate a state’s occurrence from the time of its represented content; narrating a belief does not establish when it was acquired.
- **Representation and reference:** distinguish an object from propositions about it, scene presence from representational mode, and thought from action. Representing the absent mare establishes neither memory nor a retrieval mechanism. Higher-order reflection must link directly to the state it concerns.
- **Experience and uncertainty:** distinguish perception, attention, sensation, affect, belief, imagination, appraisal, questioning, deliberation, intention, decision, and action where supported. Preserve the text’s experiential qualities, negation, modality, and alternatives; leave unsupported specifics unknown.
- **Interpretation and continuity:** retain irony, metaphor, self-presentation, and possible coping. Keep creator intentions attributed and imagined events hypothetical. Label Cove’s later feedback as interpretation. Preserve earlier states when later ones change; neither becomes a permanent trait by default.
- **Implementation responsibility:** the agent performs annotation and source checking. Bring the author only genuine interpretive decisions, with evidence and a recommendation.

## Data representation


### Cause and effect is a core requirement

The map must represent both what each character state is and what brings it about or follows from it. Causal analysis runs alongside reference and state classification in every implementation milestone.

Track physical plot causes (the spilled crate releases apples), perceptual conditions (the apple is at Cove’s boot when he looks down), connections between representations (the rotting apple and the neglected mare become relevant to one another), reasons that motivate deliberation and action, and affective consequences (imagining the players at lunch brings some comfort). Use the passage to identify which relation is supported in each case.

For every proposed cause-and-effect connection, store the source event or state, the resulting event or state, supporting sentence spans, and whether the causal account is explicit in the text, inferred from the passage, or attributed to Cove. The source can be an inner representation: an external event is not required for a thought to prompt reflection, appraisal, or an emotional response.

The first apple-sequence deliverable must include supported causal connections. Map how the mare representation participates in deliberation without claiming how Cove originally learned about her.

Extend `data/state-notes.json` into the authoritative annotation source while retaining the readable notes already there. Migrate its schema deliberately; keep the current sentence IDs and source evidence. `data/sentences.json` and the readable review remain generated outputs.

| Record | Required information |
|---|---|
| Entity | Readable identity; source mentions; aliases with supporting context. Do not equate the player, creator, and viewer without evidence. |
| Event | Actor, action, participants, source spans, actual/reported/possible status, and position in the story. |
| Character state | Holder, kind, readable description, content/object, scene presence, representational mode, source spans, explicit/inferred basis, state occurrence time, represented content time, and unspecified information origin where relevant. |
| Higher-order state | The same fields plus an explicit target state. Preserve ambiguous target candidates when needed. |
| Relation | Source, target, relation type, source evidence, attribution, and explicit/inferred/uncertain status. |
| Interpretation | What is inferred, why, supporting and potentially conflicting passages, and whether it comes from the chapter reading or Cove’s later feedback. |

A graph node can be an entity, event, or character state. Proposed relation vocabulary starts with `refers_to`, `has_content`, `reflects_on`, `precedes`, `coexists_with`, `revises`, `supports`, `motivates`, `enables`, `causes`, and `performs`. These labels must be defined in code and validated. Add a relation only when it expresses a distinction needed in the text. `Precedes` never implies `causes`.

## Quality checks and completion criteria

- Verify source hash, exact spans, full source-unit coverage, and reproducible rebuilds.
- Require a holder, kind, content/target, and evidence for every character state. Preserve unknowns and the distinctions between state/content time and scene presence/representational mode.
- Resolve graph endpoints; higher-order links must target states. Preserve ambiguous references explicitly.
- Check interpretation boundaries: imagined lunch stays imagined, creator intent stays attributed, and the apple’s gaze stays figurative. Retain conflicting and changing states.
- Validate causal evidence and attribution separately from chronology; adjacency alone cannot establish a cause.
- Compare Python and PyTorch query results, including unknowns, inferred links, empty relations, and repeated references. Every result must trace to readable records and source evidence.

The complete build lets a reader select a sentence or object and inspect events, representations, higher-order targets, causal connections, and changes through the chapter, with exact evidence.

## Repository footprint

Keep the chapter in `chapters/`, annotations and generated review in `data/`, implementation in `src/`, and this single plan in `docs/`. Extend existing files; add focused modules, one dependency declaration, and meaningful tests as milestones require. Generate graph/tensor artifacts from annotations and reuse the current review rather than creating additional reports.

The next implementation task is milestone 1: annotate the apple sequence using the agreed granularity.
