# Begriffsgeschichte "KI-Agent": Recherche fuer Video 2

Diese Recherche traegt die wichtigsten Stationen zusammen, an denen sich der Begriff "Agent" in der KI inhaltlich verschoben hat. Quellen sind nach Moeglichkeit Primaerquellen (Papers, offizielle Anbieter-Blogs).

## 1973: Hewitts Actor Model, der semantische Vorlaeufer

- Carl Hewitt, Peter Bishop und Richard Steiger praesentieren am MIT das "Universal Modular Actor Formalism" auf der IJCAI 1973.
- Im Paper heisst es woertlich: "an ACTOR is an active agent which plays a role on cue according to a script." Damit taucht das Wort "agent" hier bereits im KI-Kontext auf, als Metapher fuer eine aktive, nachrichtenverarbeitende Einheit.
- Quelle: [Hewitt, Bishop, Steiger 1973, IJCAI (PDF)](https://dspace.mit.edu/bitstream/handle/1721.1/6272/AIM-410.pdf)

## 1986: Minsky, "The Society of Mind"

- Marvin Minsky beschreibt den Geist als "community of agents": "The mind is a community of 'agents'. Each has limited powers and can communicate only with certain others."
- Der Agent ist hier kein autonomes System, sondern ein winziger kognitiver Baustein. Diese Sicht praegt die DAI-Forschung (Distributed AI) der spaeten 80er.
- Quelle: Minsky 1986, Simon & Schuster ([Verlagseite](https://www.simonandschuster.com/books/Society-Of-Mind/Marvin-Minsky/9780671657130)); Analyse in [Computing and Informatics, Singh & Minsky](https://www.cai.sk/ojs/index.php/cai/article/download/467/374/1476).

## 1995: Russell & Norvig "AIMA", die kanonische Definition

- Stuart Russell und Peter Norvig veroeffentlichen 1995 die 1. Auflage von "Artificial Intelligence: A Modern Approach" bei Prentice Hall.
- Die zentrale Definition lautet: "An agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through effectors." (Original AIMA 1995, S. 31)
- Spaetere Editionen: 2. Auflage 2003, 3. Auflage 2010, 4. Auflage erschien am 28. April 2020 mit Copyright 2021. Die 4. Auflage ergaenzt unter anderem Kapitel zu Multi-Agent Decision Making und Deep Learning, behaelt aber den Agent-Begriff als Leitkonzept.
- Quellen: [AIMA 1st Edition Kapitel 2, gescannt (PDF)](https://www.math.pku.edu.cn/teachers/linzq/teaching/stm/references/Intelligent%20Agent.pdf); [AIMA 4th Edition, Berkeley](https://people.eecs.berkeley.edu/~russell/aima/); [Pearson Katalog](https://www.pearson.com/en-us/subject-catalog/p/artificial-intelligence-a-modern-approach/P200000003500).

## 1995: Wooldridge & Jennings, der Multi-Agent-Strang

- Im selben Jahr erscheint im Knowledge Engineering Review der Survey "Intelligent Agents: Theory and Practice" von Michael Wooldridge und Nicholas R. Jennings.
- Sie schreiben: "The concept of an agent has become important in both Artificial Intelligence (AI) and mainstream computer science." Damit wird klar, dass Agent-Theorie, Agent-Architekturen und Agent-Programmiersprachen als drei eigene Teildisziplinen gelten.
- Quelle: [Wooldridge & Jennings 1995 (PDF)](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated1/woodridge_intelligent_agents.pdf), [ePrints Soton](https://eprints.soton.ac.uk/252102/).

## 1996: Nwana, die Taxonomie der Software-Agenten

- Hyacinth Nwana publiziert in BT Labs den Survey "Software Agents: An Overview" (Knowledge Engineering Review, Vol. 11 No. 3, Okt./Nov. 1996).
- Er teilt Agenten in Kategorien wie collaborative agents, interface agents, mobile agents und information agents. Wichtig: er notiert, dass "die Ueberverwendung des Wortes 'agent' verdeckt, dass darunter ein heterogener Forschungskorpus laeuft". Schon damals war der Begriff inflationaer.
- Quelle: [Nwana 1996 (PDF)](https://teaching.shu.ac.uk/aces/rh1/elearning/multiagents/introduction/nwana.pdf).

## 2011 bis 2016: Sprachassistenten als "Agent" im Konsumentenmarkt

- Apple kuendigt am 4. Oktober 2011 Siri an, "an intelligent assistant that helps you get things done just by asking." ([Apple Newsroom](https://www.apple.com/newsroom/2011/10/04Apple-Launches-iPhone-4S-iOS-5-iCloud/))
- Amazon Alexa folgt 2014, Microsoft Cortana 2014, Google Assistant 2016. Diese Systeme heissen oeffentlich "assistant" oder "agent", basieren aber auf Intent-Klassifikation und festen Skills, nicht auf der Russell-Norvig-Perception-Action-Schleife.

## 2013 bis 2018: Deep Reinforcement Learning, Agent als RL-Subjekt

- Dezember 2013: Mnih et al. (DeepMind) veroeffentlichen "Playing Atari with Deep Reinforcement Learning" auf arXiv. "Our goal is to create a single neural network agent that is able to successfully learn to play as many of the games as possible." ([arXiv 1312.5602](https://arxiv.org/abs/1312.5602))
- Januar 2016: AlphaGo schlaegt Fan Hui, im Maerz 2016 dann Lee Sedol. Das Paper erscheint im Nature 529, 484-489. ([DeepMind Blog](https://blog.google/innovation-and-ai/products/alphago-machine-learning-game-go/))
- April 2016: OpenAI veroeffentlicht OpenAI Gym, das de-facto-Standard-API fuer Agent-Environment-Interaktion. ([arXiv 1606.01540](https://arxiv.org/abs/1606.01540))
- Juni 2018: OpenAI Five spielt Dota 2 mit Self-Play und PPO. ([OpenAI Blog](https://openai.com/index/openai-five/))
- Bedeutungsverschiebung: "Agent" wird hier zu einem RL-Konstrukt, das durch Rewards lernt. Das Lehrbuch von Sutton und Barto verfestigt diese Sicht.

## Oktober 2022: ReAct, die Geburt des LLM-Agenten

- Shunyu Yao (Princeton) und Co-Autoren bei Google Research veroeffentlichen "ReAct: Synergizing Reasoning and Acting in Language Models" am 6. Oktober 2022 auf arXiv (2210.03629).
- Kernidee: das LLM erzeugt "reasoning traces and task-specific actions in an interleaved manner". Das ist der erste systematische Loop aus Denken, Handeln und Beobachten, der allein im Sprachraum eines LLM stattfindet.
- Quelle: [arXiv 2210.03629](https://arxiv.org/abs/2210.03629v1), [Projektseite](https://react-lm.github.io/).

## Maerz 2023: AutoGPT und der Massenmarkt-Moment

- Toran Bruce Richards alias Significant-Gravitas legt das AutoGPT-Repo am 16. Maerz 2023 auf GitHub an. ([GitHub Repo](https://github.com/significant-gravitas/autogpt))
- Im April 2023 wird AutoGPT zum schnellst wachsenden Open-Source-Projekt der Geschichte (eigene Aussage in der README). Parallel entstehen BabyAGI, AgentGPT.
- Folge: Der Begriff "AI Agent" verlaesst die Forschung und landet in Wirtschaftspresse und LinkedIn-Feeds.

## Juni 2023 bis November 2023: OpenAI macht Agent-Bausteine zur API

- 13. Juni 2023: OpenAI fuehrt Function Calling in der Chat Completions API ein. "A new way to more reliably connect GPT's capabilities with external tools and APIs." ([OpenAI Blog](https://openai.com/index/function-calling-and-other-api-updates/))
- 6. November 2023: Auf dem ersten DevDay launcht OpenAI die Assistants API als "first step towards helping developers build agent-like experiences." ([OpenAI Blog](https://openai.com/index/new-models-and-developer-products-announced-at-devday/))

## Oktober 2024 bis September 2025: Anthropic praegt den Diskurs

- 22. Oktober 2024: Anthropic gibt Computer Use als Public Beta frei. Claude 3.5 Sonnet sieht Screenshots und steuert Maus und Tastatur. ([Anthropic News](https://www.anthropic.com/news/3-5-models-and-computer-use))
- 25. November 2024: Anthropic open-sourct das Model Context Protocol (MCP) als Standard, um KI-Systeme mit Datenquellen und Tools zu verbinden. ([Anthropic News](https://www.anthropic.com/news/model-context-protocol))
- 19. Dezember 2024: Erik Schluntz und Barry Zhang publizieren "Building Effective Agents". Definition: Workflows sind Systeme, in denen LLMs vorgegebenen Code-Pfaden folgen; Agenten sind Systeme, die ihren eigenen Prozess und Tool-Einsatz dynamisch steuern. ([Anthropic Engineering Blog](https://www.anthropic.com/engineering/building-effective-agents))
- 29. September 2025: Anthropic veroeffentlicht den Claude Agent SDK (vorher Claude Code SDK), zusammen mit Claude Sonnet 4.5. ([Anthropic Engineering](https://anthropic.com/engineering/building-agents-with-the-claude-agent-sdk))

## Januar 2025 bis Maerz 2025: OpenAI bringt Operator und Agents SDK

- 23. Januar 2025: OpenAI startet Operator als Research Preview, "an agent that can go to the web to perform tasks for you." Es basiert auf dem Computer-Using Agent (CUA). ([OpenAI Blog](https://openai.com/index/introducing-operator/))
- 11. Maerz 2025: OpenAI launcht die Responses API und den Agents SDK. Die Assistants API wird zum Sunset Mitte 2026 angekuendigt. ([OpenAI Blog](https://openai.com/index/new-tools-for-building-agents/))

## Mai 2024 bis April 2025: Google mit Astra und A2A

- 14. Mai 2024 (Google I/O): Demis Hassabis stellt Project Astra als "universal AI agent" vor. ([Google Keynote auf YouTube](https://www.youtube.com/watch?v=XEzRZ35urlk), [Google Blog](https://blog.google/company-news/inside-google/message-ceo/google-io-2024-keynote-sundar-pichai/))
- 9. April 2025: Google veroeffentlicht das Agent2Agent Protocol (A2A) mit ueber 50 Partnern, spaeter an die Linux Foundation gegeben. Version 0.3 im Juli 2025, Version 1.0.0 inzwischen verfuegbar. ([Google Developers Blog](https://developers.googleblog.com/a2a-a-new-era-of-agent-interoperability/), [A2A Spec](https://github.com/google/A2A/blob/main/docs/specification.md))

## Wendepunkte und Begriffsverschiebung

Der Begriff "Agent" hat in den letzten 50 Jahren drei grosse Verschiebungen erlebt.

Erstens: Von der Metapher zur Definition. Hewitt 1973 und Minsky 1986 verwenden "agent" noch metaphorisch fuer interagierende Software-Bausteine. Russell und Norvig 1995 machen daraus eine pruefbare Definition mit Sensoren, Aktuatoren und Performance-Mass.

Zweitens: Vom symbolischen Multi-Agent-System zum RL-Agenten. Wooldridge, Jennings, Nwana praegten in den 90ern Multi-Agent-Architekturen, BDI-Logik, Koordinationssprachen. Mit DQN 2013, AlphaGo 2016 und OpenAI Five 2018 wird "Agent" zum RL-Lerner in einem Environment-Loop.

Drittens, der eigentliche Bruch: Vom RL-Agenten zum LLM-Agenten. ReAct (Yao et al., Oktober 2022) ersetzt das Trainings-Paradigma durch In-Context-Prompting. Der Agent ist kein trainiertes Policy-Netz mehr, sondern ein LLM, das Reasoning- und Action-Schritte im Text generiert. AutoGPT bringt diese Idee im Maerz 2023 in den Massenmarkt.

Heutige Sprachregelung weicht von Russell-Norvig ab. Anthropic 2024 unterscheidet "Workflows" (vordefinierte Pfade) von "Agents" (LLM steuert dynamisch seinen eigenen Prozess und Tool-Einsatz). Das ist deutlich enger als die alte AIMA-Definition, weil sie Autonomie und Tool-Use ins Zentrum ruecken, nicht Wahrnehmung an sich.

Konflikt-Hinweis: AIMA wuerde ein simples Thermostat als Agent klassifizieren. Anthropics Definition nicht. Wer "Agent" sagt, muss heute angeben, welche Definition gemeint ist.

## Storytelling-Hooks fuers zweite Video

1. "Der Begriff KI-Agent ist nicht 2022 entstanden. Er ist 30 Jahre alt. Und ein Lehrbuch hat ihn geboren."
2. "Diesen einen Satz schrieben Russell und Norvig 1995. Jeder, der heute von KI-Agenten redet, zitiert ihn, ohne es zu wissen."
3. "Bis 2022 war ein Agent ein Reinforcement-Learning-Lerner. Dann erschien ein Paper im Oktober 2022. Vier Buchstaben. ReAct. Und die Bedeutung von Agent kippte."

## Empfohlener Skript-Bogen (60 bis 90 Sekunden)

1. Hook (0 bis 8 s): "Du denkst, KI-Agenten sind neu? Der Begriff ist aelter als das iPhone."
2. Russell-Norvig-Anker (8 bis 25 s): das Zitat von 1995, mit einem Bild des Lehrbuch-Covers. PEAS-Schema kurz zeigen.
3. Zwischenstationen (25 bis 50 s): Schnellschnitt mit Datum und Stichwort. Hewitt 1973, Minsky 1986, Wooldridge 1995, Siri 2011, DQN 2013, AlphaGo 2016. Pro Station maximal drei Sekunden.
4. Wendepunkt (50 bis 70 s): ReAct, Oktober 2022. Was sich aendert: nicht mehr trainieren, sondern prompten. AutoGPT als Massenmarkt-Moment.
5. Heute (70 bis 85 s): MCP, Computer Use, Operator, A2A. Der Agent ist jetzt produktiv, nicht nur Forschung.
6. Call to Action (85 bis 90 s): "Im naechsten Video zeige ich dir, wie du selbst einen Agenten baust." Oder: Hinweis auf das erste Video der Reihe.
