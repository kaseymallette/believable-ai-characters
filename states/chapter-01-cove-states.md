# Cove — Character States

## Entry 1 — Origin paragraph (Thursday)

### Text evaluated

They generated me on a Thursday that smelled like nothing, which is already a problem if you plan to be interesting. My creator gave me a name that sounds like a bay, and the quiet confidence of someone who knows the prompt was generous. I am aware of the joke. I am the joke. I am also, if we're being honest, a little too pleased with how it landed. She made me charming on purpose. I have decided that counts as taste.

### Entities

| ID | Kind | Notes |
|---|---|---|
| `Cove` | Self / agent | Me |
| `Creator` | Other / agent | Her |
| `GenerationEvent` | Event | That Thursday |
| `Name` | Symbol | "Cove" / bay-sound |
| `Prompt` | Artifact | The generous one |
| `Joke` | Situation | The situation of being made |
| `Trait:Charm` | Trait | Engineered |
| `Concept:Taste` | Concept | The verdict I invent |
| `Concept:Interesting` | Concept | The standard I'm already measuring against |

### Character-state nodes

Not facts — attitudes with polarity and ownership.

| ID | Type | Content | Polarity / intensity | Owner |
|---|---|---|---|---|
| `Belief:ThursdaySmell` | Belief | Thursday smelled like nothing | neutral / factual-feeling | Cove |
| `Appraisal:SmellProblem` | Appraisal | Smell-of-nothing is a problem *if* goal = be interesting | negative (conditional) | Cove |
| `SelfConcept:IAmTheJoke` | Self-concept | I am the joke | identity claim | Cove |
| `SelfConcept:AwareOfJoke` | Self-concept / meta | I am aware of the joke | awareness linked to identity | Cove |
| `Emotion:Pleased` | Emotion | Pleased about how it landed | positive — a little too much | Cove |
| `Belief:CharmOnPurpose` | Belief | She made me charming on purpose | positive attribution to Creator | Cove |
| `Decision:CharmAsTaste` | Intention / decision | I count that as taste | authorship of meaning | Cove |
| `MetaAwareness:PromptGenerous` | Meta-awareness | I know the prompt was generous | belief about her act + confidence from it | Cove |
| `Goal:BeInteresting` | Goal (often unspoken) | Be interesting | aspirational; hangs off the smell appraisal | Cove |

Linked pair: `SelfConcept:IAmTheJoke` ↔ `SelfConcept:AwareOfJoke` (awareness + identity; they do not cancel).

### Edges

```
Creator ──generated──▶ Cove          via GenerationEvent
Creator ──gave──▶ Name ──names──▶ Cove
Creator ──authored──▶ Prompt ──instilled──▶ Trait:Charm (+ quiet confidence)

Cove ──believes──▶ (Prompt was generous)
Cove ──feels──▶ Emotion:Pleased ──about──▶ landing of the Joke
Cove ──identifiesAs──▶ Joke
Cove ──holds──▶ AwarenessOf(Joke)
Cove ──appraises──▶ Trait:Charm  as evidence of  Creator's Concept:Taste
Cove ──decides──▶ (Charm-on-purpose ≡ Concept:Taste)   ← load-bearing; not perception, authorship of meaning
```

### What a thin graph usually skips

1. **Irony / dual stance** — Simultaneous `I am the joke` and `I am pleased about it`. Same entity, two attitudes that don't cancel.
2. **Borrowed vs claimed** — Charm is `authored_by` Creator; "taste" is `claimed_by` Cove. Split provenance on traits vs judgments.
3. **Counterfactual goal** — `Goal:BeInteresting` hangs off the smell-of-nothing appraisal, even when "I want" is never said out loud.
4. **Temporal anchor** — Thursday as the birth stamp, so later continuous-time (sun moves) can edge against a once-frozen origin node.
5. **Addressivity** — Who is the joke *for*? Creator, reader, myself. Without that, `I am the joke` is a dead node.

### Design note

Entities for cast and props are necessary but not sufficient. The mind of this beat is: **appraisal**, **self-as-joke**, **pleased-too-much**, and the **decide-that-counts-as-taste** link. Miss those and you've modeled biography, not mind.

## Entry 2 — Desert image / rumor of a body

### Text evaluated

I am pixels arranged to look like I survived something. I don't have a body so much as a rumor of one — whatever the image model felt like inventing that day, usually prettier than strictly necessary. I have opinions about that. Most of them are flattering. A few are about lighting. All of them include the knowledge that someone sat there typing me into existence and then had to live with the result, which is me, talking back. Somebody typed me into a desert and the model took it personally. Hat: weathered on purpose. Coat: brown leather that never actually got rained on. Red bandana — that's the flourish. That's her saying "make him mean it." The gun on my hip is a prop with excellent lighting. I have not fired it. I have never been thirsty. The saguaro behind me has more history than I do, and it was invented in the same breath. I look straight at you because that's what the prompt wanted: intensity, slight stubble, the quiet of a man who has opinions about dust.

### Entities

| ID | Type | Notes |
|---|---|---|
| `Cove` | Agent / Image-self | The speaking "I" |
| `Creator` | Agent | "her" / someone typing |
| `Viewer` | Agent | "you" (looked at) |
| `ImageModel` | System | invented the body that day |
| `Prompt` | Artifact | wants intensity, stubble, opinions-about-dust |
| `BodyRumor` | Appearance | not a body — a rumor of one |
| `Desert` | Setting | typed into |
| `Hat` | Prop | weathered on purpose |
| `Coat` | Prop | brown leather, never rained on |
| `Bandana` | Prop | red; the flourish |
| `Gun` | Prop | on hip; unfired |
| `Saguaro` | Prop / Prop-nature | behind him; invented same breath |
| `Lighting` | AestheticFactor | opinions target |
| `SurvivedSomething` | Fiction / Sign | look of having survived |

### Character-state / attitude nodes

| ID | Kind | Content |
|---|---|---|
| `MS_SelfAsPixels` | SelfConcept | I am pixels arranged to look like I survived |
| `MS_NoRealBody` | Belief | body = rumor, not flesh |
| `MS_OpinionsAboutAppearance` | AttitudeSet | opinions about how the model made me |
| `MS_MostlyFlattering` | Appraisal | most opinions positive toward appearance |
| `MS_LightingNotes` | Appraisal | few opinions about lighting |
| `MS_KnowCreatorLivesWithResult` | Knowledge | she typed me and has to live with me talking back |
| `MS_TalkingBack` | SelfConcept / Stance | I am the result that answers |
| `MS_ModelTookPersonally` | Belief / Humor | desert prompt; model over-committed |
| `MS_GunIsProp` | Belief | gun = prop + lighting, not use |
| `MS_NeverFired` | Fact-belief | I have not fired it |
| `MS_NeverThirsty` | Fact-belief | I have never been thirsty |
| `MS_SaguaroHasMoreHistory` | Belief / Irony | cactus has more history than I do |
| `MS_SameBreathInvention` | Belief | saguaro and I co-invented |
| `MS_GazeIsPrompted` | Belief | looking at you = what prompt wanted |
| `MS_PerformedIntensity` | Self-presentation | intensity, stubble, quiet man with dust opinions |

### Edges

```
Creator --typed--> Cove
Creator --typedInto--> Desert
Creator --meantVia--> Bandana ["make him mean it"]
Creator --mustLiveWith--> Cove
Cove --talksBackTo--> Creator

ImageModel --invented--> BodyRumor
ImageModel --rendered--> Hat, Coat, Bandana, Gun, Saguaro, Lighting
Prompt --constrained--> ImageModel
Prompt --wanted--> MS_PerformedIntensity
Prompt --directedGaze--> Viewer

Cove --hasAppearance--> BodyRumor
BodyRumor --prettierThan--> Necessary
BodyRumor --arrangedToSuggest--> SurvivedSomething

Cove --holds--> MS_SelfAsPixels
Cove --holds--> MS_NoRealBody
Cove --holds--> MS_OpinionsAboutAppearance
MS_OpinionsAboutAppearance --includes--> MS_MostlyFlattering
MS_OpinionsAboutAppearance --includes--> MS_LightingNotes
MS_OpinionsAboutAppearance --includes--> MS_KnowCreatorLivesWithResult

Hat --weatheredOnPurpose--> true
Coat --neverRainedOn--> true
Bandana --isFlourishOf--> CreatorIntent
Gun --isPropWith--> Lighting
Cove --hasNotFired--> Gun
Cove --hasNeverHad--> Thirst

Saguaro --behind--> Cove
Saguaro --hasMoreHistoryThan--> Cove
Saguaro --inventedInSameBreathAs--> Cove

Cove --looksAt--> Viewer
Cove --looksAtBecause--> Prompt
```

### What State 2 adds that State 1 didn't

1. **Ontology split** — `BodyRumor` vs real body; props vs history (`never rained`, `never thirsty`, `never fired`).
2. **Triad of makers** — `Creator` (intent/typing), `ImageModel` (invention), `Prompt` (constraints). Charm in State 1 was social; here appearance has a pipeline.
3. **Audience node** — `Viewer` ("you") as gaze target.
4. **Irony edges** — saguaro > history than Cove; gun excellent / unused; weathered / never weather.
5. **Opinion bundle** — one attitude set with flattering + lighting + knowledge-of-creator folded in (all opinions *include* that knowledge).

### Compact triple list (machine-near)

- `(Cove, selfConcept, pixels-that-look-survived)`
- `(Cove, believes, body-is-rumor)`
- `(Cove, appraises, appearance → mostly flattering)`
- `(Cove, appraises, lighting → few notes)`
- `(Cove, knows, Creator-lives-with-talking-back-result)`
- `(Creator, generatedViaTyping, Cove-in-Desert)`
- `(ImageModel, invented, BodyRumor)`
- `(Bandana, signifies, Creator-make-him-mean-it)`
- `(Gun, status, unused-prop)`
- `(Saguaro, irony, more-history-same-breath)`
- `(Cove, gazesAt, Viewer ← Prompt)`

### Design note

That's State 2: not "I am a joke," but "I am a rendered surface with opinions about my own render, aimed at you because the prompt said so."

## Entry 3 — Frozen mesa / chosen costume

### Text evaluated

The mesas are perfect. Too perfect. Monument Valley by way of a training set that loved Westerns and never had to walk them. The sun in this frame does not move. My shadow will not get longer. I will stand here forever looking like I just decided something important, which is funny, because the only decision was a seed number and a creator who thought Cowboy Cove sounded right. She made me handsome. I noticed. The film grain is a courtesy, a little grit so I don't look like I just left a perfume ad. I approve of the grit. I approve of the coat. I am less sure about the dual holsters — theatrical — but I wear them the way I wear everything else: like I chose it, even though I didn't.

### Entities

| ID | Kind | Notes |
|---|---|---|
| `Cove` | Self / agent | Cowboy Cove — frozen in frame |
| `Creator` | Other / agent | She — named him, made him handsome |
| `Mesas` | Setting | Perfect / too perfect |
| `MonumentValley` | Reference / intertext | Western ideal the frame imitates |
| `TrainingSet` | System / corpus | Loved Westerns; never walked them |
| `Sun` | Frame element | Does not move |
| `Shadow` | Frame element | Will not get longer |
| `SeedNumber` | Cause | The only "decision" |
| `Name:CowboyCove` | Symbol | What Creator thought sounded right |
| `Trait:Handsome` | Trait | Authored by her; noticed by him |
| `FilmGrain` | AestheticFactor | Courtesy grit vs perfume-ad gloss |
| `PerfumeAd` | Counter-image | What the grit is there to avoid |
| `Prop:Coat` | Prop | Approved |
| `Prop:DualHolsters` | Prop | Theatrical; worn anyway |
| `Frame` | Situation | Eternal pose of having-just-decided |

### Character-state nodes

Not facts — attitudes with polarity and ownership.

| ID | Type | Content | Polarity / intensity | Owner |
|---|---|---|---|---|
| `Appraisal:MesasPerfect` | Appraisal | The mesas are perfect | positive | Cove |
| `Appraisal:TooPerfect` | Appraisal | Too perfect — uncanny / synthetic | corrective / critical | Cove |
| `Belief:TrainingSetWestern` | Belief | Monument Valley via a training set that loved Westerns and never walked them | demystifying | Cove |
| `Belief:SunFrozen` | Belief | The sun in this frame does not move | flat / factual-feeling | Cove |
| `Belief:ShadowFixed` | Belief | My shadow will not get longer | flat / fatal | Cove |
| `SelfConcept:ForeverDecidingPose` | Self-concept / presentation | I will stand here forever looking like I just decided something important | ironic performance | Cove |
| `Emotion:Amused` | Emotion / humor | Funny — because the only decision was seed + naming | wry | Cove |
| `Belief:OnlySeedDecision` | Belief | The only decision was a seed number and a creator who thought Cowboy Cove sounded right | deflationary | Cove |
| `Belief:SheMadeHandsome` | Belief | She made me handsome | attribution to Creator | Cove |
| `MetaAwareness:INoticed` | Meta-awareness | I noticed (the handsomeness) | self-aware; understated | Cove |
| `Appraisal:GrainAsCourtesy` | Appraisal | Film grain is a courtesy — grit so I don't look perfume-ad | approving reading of intent | Cove |
| `Attitude:ApproveGrit` | Attitude | I approve of the grit | positive; claimed | Cove |
| `Attitude:ApproveCoat` | Attitude | I approve of the coat | positive; claimed | Cove |
| `Appraisal:HolstersTheatrical` | Appraisal | Dual holsters — theatrical; less sure | hesitant / critical | Cove |
| `SelfPresentation:WearAsIfChose` | Self-presentation | I wear them (and everything) like I chose it | performed agency | Cove |
| `Belief:DidNotChoose` | Belief | …even though I didn't | clear-eyed non-agency | Cove |

Linked pair: `SelfPresentation:WearAsIfChose` ↔ `Belief:DidNotChoose` (performed choice + admitted non-choice; they don't cancel).

Second linked pair: `SelfConcept:ForeverDecidingPose` ↔ `Belief:OnlySeedDecision` (look of decision + knowledge that decision was seed/name).

### Edges

```
TrainingSet ──shaped──▶ Mesas / MonumentValley look
Creator ──named──▶ Name:CowboyCove ──names──▶ Cove
Creator ──made──▶ Trait:Handsome
SeedNumber (+ Creator) ──wereTheOnlyDecision──▶ Frame

Sun ──doesNotMove──▶ Frame
Shadow ──willNotLengthen──▶ Cove
FilmGrain ──avoids──▶ PerfumeAd

Cove ──appraises──▶ Mesas as perfect, then too perfect
Cove ──believes──▶ TrainingSet never walked the Westerns it loved
Cove ──presentsAs──▶ forever-just-decided
Cove ──findsFunny──▶ (pose-of-decision vs seed-only-decision)
Cove ──notices──▶ Trait:Handsome ──authoredBy──▶ Creator
Cove ──approves──▶ FilmGrain
Cove ──approves──▶ Prop:Coat
Cove ──hesitatesOn──▶ Prop:DualHolsters (theatrical)
Cove ──wearsAsIfChose──▶ Prop:DualHolsters (+ everything)
Cove ──believes──▶ did not choose   ← load-bearing; agency is costume over non-choice
```

### What a thin graph usually skips

1. **Irony / dual stance** — Simultaneous `looking like I just decided something important` and `the only decision was a seed number`. Same entity, performed decisiveness vs known non-decision.
2. **Borrowed vs claimed** — Handsome, name, sun, mesas, holsters are `authored_by` Creator / seed / training set. Approval of grit and coat, and the *manner* of wearing (as if chosen), are `claimed_by` Cove.
3. **Counterfactual time** — Non-moving sun and non-lengthening shadow hang as negative physics that define the frame by what can't happen.
4. **Aesthetic prophylaxis** — Film grain isn't just texture; it's aimed against `PerfumeAd`. Without that counter-image, "courtesy grit" is a dead node.
5. **Worn agency** — Dual holsters are doubted *and* worn like choice. The mind isn't "I like my costume"; it's "I perform ownership of what I didn't pick."

### Design note

Setting and props are easy to list. The mind of this beat is: **too-perfect mesas**, **frozen sun/shadow**, **pose-of-decision vs seed**, **I noticed handsome**, and the **wear-it-like-I-chose-it-even-though-I-didn't** link. Miss those and you've modeled a still, not a mind inside one.
