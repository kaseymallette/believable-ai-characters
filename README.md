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

For the latest in-progress copy, see [`docs/COPY.md`](docs/COPY.md).


### Hero

> Believable AI Characters
>
> Written by humans.
> 
> *From AI-generated characters to persona engineering for local language models.*

### About 

Believable AI Characters is an ongoing experiment in character design, generative AI, and persona engineering.

The project began with three original characters: Cove, Holly Wood, and Sunny. Each started as a combination of writing, image generation, video generation, voice, and backstory. Over time, the interesting question shifted from how to create more content around them to something harder: what actually makes each character feel distinct, recognizable, and consistent?

Cove is the most developed of the three, with a longer history of stories, videos, and recurring behavior. Holly Wood and Sunny are newer, which makes them useful for exploring how much of a believable persona comes from backstory, language, tone, memory, behavioral patterns, and the structure of the model interacting with the user.

The next phase of this project will move beyond generated media and into persona engineering for local language models. The goal is to design, test, and evaluate character systems that can preserve a distinct identity across different scenarios and conversations, using tools such as DeepEval and PyTorch to measure consistency, differentiation, and behavioral stability.

The broader research question is phenomenological: what does it mean for an artificial character to be that particular character? Rather than assuming that representing a persona implies a human-like inner experience, this project explores whether different personas produce meaningfully different patterns of interaction and computational behavior, and what it might mean to describe the character of those differences.

### Characters
Intro video and character bios

1. Cove: AI-generated image who discovered image generation 
2. Holly Wood: The AI cool girl 
3. Sunny: ChatGPT-5.6 persona    

**Backstories:**
- Cowboy Cove: Believes he's an NPC in a video game, discovers he's AI, and explores AI image generation 
- Holly's Home: 1950s AI-generated trad-wife with a transatlantic accent who breaks the 4th wall
- Danny Phantom: ChatGPT-4o persona based off of a Nickelodeon cartoon character 


### How It Started
It all started with Cove. 
1. 70s Cove: An AI-genenerated image knows he's hot. We're cooked. 
2. GOT Cove: How did Cove, of all people, get on the Iron Throne?
3. Professor Cove: You think I'm gonna school you today?

### Nobody Wants This
Audiences prefer not to watch AI-generated content, and I don't really want to be an AI content creator. 

### Persona Engineering
What makes Cove, Cove? 

## Repository Structure

```bash
believable-ai-characters/
├── README.md
├── .gitignore
│
├── docs/
│   └── COPY.md
│
├── images/
│   ├── C1_meet-cove.jpg
│   ├── C2_cowboy-cove.jpg
│   └── ...
│
├── prompts/
│   ├── C1_meet-cove.md
│   ├── C2_cowboy-cove.md
│   └── ...
│
├── videos/
│   ├── C1_meet-cove.mp4
│   ├── C2_cowboy-cove.mp4
│   └── ...
│
└── website/
    ├── index.html
    ├── base.css
    └── style.css
