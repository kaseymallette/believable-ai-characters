# believable-ai-characters

Believable AI Characters is a storytelling portfolio and research project about how an AI character becomes recognizable across images, video, writing, and interaction. It follows three original characters—Cove, Holly Wood, and Sunny—and asks what gives each one a distinct voice and history. I used Grok Imagine to generate their images and videos, and I’m using Grok Bot to develop their written stories. 

Current development focuses on writing chapters and mapping character States. The planned persona-engineering phase will use PyTorch, TensorFlow, and DeepEval to build and evaluate personas for local language models.

[Watch on YouTube](https://www.youtube.com/@KCatthebat)

## In Development

Website copy is maintained in `website/COPY.md`. Current development is focused on persona engineering.

## Website Structure
- Hero
- About
- Characters
- Story
- Technical Implementation

For the latest in-progress copy, see [`website/COPY.md`](website/COPY.md).


## Hero

> Believable AI Characters
>
> Written by humans.
> 
> *From AI-generated characters to persona engineering for local language models.*

## About 

Believable AI Characters is an ongoing experiment in character design, generative AI, storytelling, and persona engineering.

The project began with three original characters—Cove, Holly Wood, and Sunny—created as AI-generated images and videos using Grok Imagine. Writing, voice, and backstory gave them more to say and do. Over time, the question shifted from how to make more content with them to something harder: what makes each character distinct, recognizable, and consistent?

Cove is the most developed, with a longer history of videos, stories, and recurring behavior. Holly Wood and Sunny are newer. Developing them alongside Cove creates a way to explore how backstory, language, tone, memory, and behavioral patterns contribute to a persona.

The videos now serve as starting points for written chapters. Chapter One grew from the first 30 seconds of a Cove video into a story of more than 5,000 words. Alongside the chapters, the project preserves the prompts and responses from the writing process and a paragraph-by-paragraph *States* record of what the characters believe, interpret, and revise. The prompts show how the story was made; the States follow the story as written.

The next phase will explore how to represent these developing characters for local language models. Tools such as PyTorch, TensorFlow, and DeepEval may help build and evaluate whether a persona remains recognizable and distinct across interactions.

The broader question is phenomenological: what does it mean for an artificial character to be *that particular character*? Representing a persona or an emotion does not, by itself, establish a human-like inner experience. This project examines the structure of each character’s history and interactions, and asks whether different personas can produce meaningfully different patterns as they unfold.

## Characters

![Characters](images/characters.jpg)

*Left to right: Cove, Holly Wood, Sunny.*

### Cove

**Description:** AI-generated image who discovered image generation 

### Holly Wood

**Description:** The AI cool girl

### Sunny

**Description:** A self-aware and charming AI companion, based on a ChatGPT-5.6 persona

## Repository Structure

```bash
believable-ai-characters/
├── README.md
├── .gitignore
│
├── chapters/
│   ├── chapter-01-cove.md
│   ├── chapter-01-cove.pdf
│   └── ...
│
├── images/
│   ├── characters.jpg
│   ├── cowboy-cove.jpg
│   └── ...
│ 
├── prompts/
│   ├── chapter-01-cove-prompts.md
│   └── ...
│ 
├── states/
│   ├── chapter-01-cove-states.md
│   └── ...
│     
├── videos/
│   ├── chapter-01-cove.mp4
│   └── ...
│
└── website/
    ├── base.css
    ├── COPY.md
    ├── index.html
    └── style.css
```