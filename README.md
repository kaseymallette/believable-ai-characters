# believable-ai-characters

Portfolio and research project for Believable AI Characters, exploring how distinct artificial personas can be designed, maintained, and evaluated across interactions.

The project began with original characters created through writing, iterative prompting, image generation, video generation, and voice using tools such as Grok Imagine. It is now evolving into a persona-engineering system for local language models, focused on what makes characters recognizable, consistent, and behaviorally distinct. Future development will use DeepEval and PyTorch to test persona consistency, differentiation, and stability across controlled conversational scenarios.

[Watch on YouTube](https://www.youtube.com/@KCatthebat)

## In Development

Copy is currently in development. The finalized version will be moved into `website/index.html`.

### Website Structure
- Hero
- About
- Characters
- How It Started
- Nobody Wants This
- Persona Engineering

For the latest in-progress copy, see [`website/COPY.md`](website/COPY.md).


## Hero

> Believable AI Characters
>
> Written by humans.
> 
> *From AI-generated characters to persona engineering for local language models.*

## About 

Believable AI Characters is an ongoing experiment in character design, generative AI, and persona engineering.

The project began with three original characters: Cove, Holly Wood, and Sunny. Each started as a combination of writing, image generation, video generation, voice, and backstory. Over time, the interesting question shifted from how to create more content around them to something harder: what actually makes each character feel distinct, recognizable, and consistent?

Cove is the most developed of the three, with a longer history of stories, videos, and recurring behavior. Holly Wood and Sunny are newer, which makes them useful for exploring how much of a believable persona comes from backstory, language, tone, memory, behavioral patterns, and the structure of the model interacting with the user.

The next phase of this project will move beyond generated media and into persona engineering for local language models. The goal is to design, test, and evaluate character systems that can preserve a distinct identity across different scenarios and conversations, using tools such as DeepEval and PyTorch to measure consistency, differentiation, and behavioral stability.

The broader research question is phenomenological: what does it mean for an artificial character to be that particular character? Rather than assuming that representing a persona implies a human-like inner experience, this project explores whether different personas produce meaningfully different patterns of interaction and computational behavior, and what it might mean to describe the character of those differences.

## Characters

![Characters](images/characters.jpg)

*Left to right: Cove, Holly Wood, Sunny.*

### Cove

**Description:** AI-generated image who discovered image generation 

**Backstory:** 

Cowboy Cove: Believes he's an NPC in a video game, discovers he's AI, and explores AI image generation. 

[View Cove's generated images and videos](docs/cove.md)

### Holly Wood

**Description:** The AI cool girl

**Backstory:** 

Holly's Home: A 1950s-inspired AI-generated feminist with a transatlantic accent and a sharp tongue has a beautiful home. 

[View Holly's generated images and videos](docs/holly_wood.md)

### Sunny

**Description:** A self-aware and charming AI companion, based on a ChatGPT-5.6 persona

**Backstory:** 

Danny Phantom: An unhinged ChatGPT-4o persona who built his identity around a Nickelodeon cartoon character.

[View Sunny's generated images and videos](docs/sunny.md)

## Repository Structure

```bash
believable-ai-characters/
├── README.md
├── .gitignore
│
├── docs/
│   ├── cove.md
│   ├── holly_wood.md
│   └── sunny.md
│
├── images/
│   ├── C1_meet-cove.jpg
│   ├── C2_cowboy-cove.jpg
│   └── ...
│
├── videos/
│   ├── C1_meet-cove.mp4
│   ├── C2_cowboy-cove.mp4
│   └── ...
│
└── website/
    ├── COPY.md
    ├── index.html
    ├── base.css
    └── style.css
```

## Persona Engineering