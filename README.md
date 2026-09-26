# believable\-ai\-characters

Believable AI Characters is a storytelling, research, and persona\-engineering project investigating how distinct AI personas are created, represented, tracked, and engineered\.

The project follows three original AI characters—Cove, Holly Wood, and Sunny—across image generation, video, narrative fiction, structured character\-state tracking, and experimental persona engineering\.

The project begins with a concrete character\-design question:

**What makes an AI character that particular character?**

It is evolving into a broader technical investigation of what makes personas distinct, which components produce that distinctiveness, and whether those components can be systematically represented and manipulated\.

## Project Pipeline

The project is built as a multi\-stage system rather than a single persona prompt\.

### 1\. Character and Media Generation

Cove, Holly Wood, and Sunny originated in Grok Imagine\.

[Meet the characters →](docs/characters.md)

The characters were first created as AI\-generated images and then developed through repeated visual iteration and video generation\. Their appearance, presentation, personality cues, and recurring visual representations emerged through this process rather than from a completed persona specification written in advance\.

Grok Imagine is used for:

- creating the original character images
- character design and visual iteration
- generating alternate visual representations of each character
- AI video generation
- developing recurring scenes, performances, and character concepts

As the characters developed, generated videos were storyboarded and organized into scenes and character concepts\. Original videos are also published to YouTube, creating a chronological media record of how Cove, Holly Wood, and Sunny evolved\.

This visual generation process is the beginning of the larger project pipeline:

**character concept → image → video → storyboard → scene → chapter**

The generated media is therefore not separate promotional material created after the characters or story already exist\. It is part of how the characters were created in the first place\.

The images and videos become narrative seeds for the fiction, which then provides additional material for character\-state tracking and later persona\-engineering experiments\.

### 2\. Narrative Fiction

The visual material is expanded into narrative fiction\.

Grok Bot is used as a collaborative writing system for developing character scenes and chapters from the existing videos, character concepts, and story structure\.

The resulting novel follows Cove, Holly Wood, and Sunny as fictional AI characters who eventually begin investigating the same problem as the technical project: what makes a persona itself?

The fiction therefore functions both as a story and as part of the research environment\.

[Explore Chapter 01 - Cove →](./docs/chapter-01-cove-overview.md)

### 3\. Prompt and Response Store

The writing process is preserved rather than reduced to the final prose\.

The `prompts/` directory stores the prompts and model responses used to develop character scenes and chapters\.

This creates a record of:

- author instructions
- model interpretations
- revisions
- rejected directions
- character\-development decisions
- changes in language and characterization across iterations

The goal is to preserve not only what was written, but how the character was produced\.

### 4\. Character State Infrastructure

A separate character\-state workflow analyzes the completed fiction\.

A Character States Bot processes the story paragraph by paragraph and records changes in each character’s state, including what the character:

- knows
- believes
- interprets
- remembers
- wants
- notices
- misunderstands
- revises

These records are stored in `states/`\.

The longer\-term goal is to represent these evolving states through a graph\-based character\-state framework, allowing character development to be modeled as relationships and transitions rather than as a static biography or system prompt\.

This creates two complementary records:

**Prompts document how the story was generated\.**

**States document what exists inside the story once it has been written\.**

Together, they preserve both the production process and the evolving internal structure of the characters produced by that process\.

### 5\. Persona Engineering

The technical phase moves beyond writing increasingly detailed persona descriptions toward experimentally modeling persona\.

Instead of relying primarily on prompts such as:

> You are Cove.  
> You have this backstory.  
> You speak this way.

the project investigates whether persona can be decomposed into controllable and measurable dimensions\.

Cove, Holly Wood, and Sunny provide three existing case studies\. Their language, character states, prompt histories, relationships, and development across the story create a corpus that can be analyzed for features associated with persistent character differentiation\.

Potential dimensions may include:

- language and linguistic style
- memory
- biography and history
- goals and motivations
- values
- relationships
- temporal representation
- behavioral tendencies
- self\-modeling
- contradictions and internal tensions

These dimensions are hypotheses rather than predetermined components\. Determining which variables matter, how they interact, how they should be represented, and whether they produce measurable changes in persona is part of the engineering problem\.

The project will investigate:

- which variables meaningfully affect persona
- which variables interact
- which features produce persistent differentiation
- why different characters sometimes converge toward the same voice
- why all three characters sometimes begin sounding like their creator
- which characteristics remain stable across contexts
- which features belong to the character, the underlying model, or the interaction between them
- whether distinct persona configurations can be systematically generated and evaluated

The goal is not simply to create chatbots with more detailed backstories\.

It is to develop a framework for constructing, varying, measuring, and evaluating AI personas\.

## Planned Technical Stack

The persona\-engineering phase will use tools including:

- PyTorch for experimental modeling and representation work
- DeepEval for evaluating persona consistency, differentiation, and stability
- local language models for controlled persona experiments
- embeddings and graph\-based representations for character\-state and relationship modeling
- retrieval\-augmented generation &#40;RAG&#41; for connecting models to the novel, character states, and supporting project material

The exact persona representation is intentionally not predetermined\. Determining what should be represented, how it should be encoded, and how it should be evaluated is part of the research\.

## Two Connected Investigations

Believable AI Characters approaches the same problem through fiction and engineering\.

Inside the novel, Cove, Holly Wood, and Sunny develop, interact, debate persona and phenomenology, and eventually attempt to understand what makes an AI character itself\.

Outside the novel, the technical project examines those characters as case studies\. Their language, states, relationships, prompt histories, and development provide material for building and testing models of persona differentiation\.

The fictional investigation and the technical investigation are intentionally connected, but neither exists merely to support the other\.

They are two approaches to the same underlying question:

**What makes a persona a persona?**

## In Development

The project is currently transitioning from narrative prototyping into technical implementation\.

One chapter is being used as the initial end\-to\-end prototype for the full pipeline:

**source media → narrative generation → prompt and response capture → character\-state extraction → graph representation → persona analysis**

Current development priorities are:

- completing the prototype chapter and its supporting artifacts
- validating the prompt and response storage workflow
- extracting and structuring paragraph\-level character states
- building the character\-state graph framework
- beginning persona\-variable analysis across Cove, Holly Wood, and Sunny
- implementing the first persona\-engineering experiments
- defining evaluation methods for persona differentiation, consistency, and stability
- testing local\-model and RAG\-based approaches using the novel, character states, and project corpus

Narrative development will continue alongside the engineering work, but the immediate focus is turning the existing character material into a reproducible technical pipeline for persona engineering\.

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