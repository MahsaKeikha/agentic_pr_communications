# F128 | Agentic PR and Communications | L3 Gold Standard | v1.0

A governed five-agent reference architecture for public relations and communications research, narrative development, stakeholder analysis, media planning, risk review, evidence discipline, crisis escalation, and qualified human approval.

F128 is decision-support only. It can research, organize evidence, develop narratives, map stakeholders, draft communication options, identify risks, and prepare review packages. It cannot autonomously issue press releases, contact journalists, publish statements, speak on the record, activate crisis responses, or distribute communications externally.

## Communications lifecycle

```text
Context and Evidence
        -> Narrative Architecture
        -> Stakeholder and Media Analysis
        -> Risk and Scenario Review
        -> Claims, Privacy, Confidentiality, and Provenance Review
        -> Qualified Human Communications Approval
        -> Human-Controlled External Communication
```

The workflow fails closed when required reviews are missing or when material claims, identity, outreach, confidentiality, legal, reputational, crisis, stakeholder-harm, or provenance risks remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Research Agent | Establishes facts, sources, chronology, evidence quality, and uncertainty | What is known, what is not known, and what evidence supports it? |
| Narrative Agent | Structures messages, themes, proof points, Q&A, and communication options | How can the facts be communicated accurately and coherently? |
| Stakeholder Agent | Maps audiences, media, partners, employees, customers, communities, and other affected groups | Who needs what information, through which appropriate channel? |
| Risk Agent | Identifies legal, reputational, privacy, crisis, misinformation, safety, and stakeholder risks | What could go wrong if this communication is released or delayed? |
| Review Agent | Integrates evidence, claims, risk, authority, provenance, and approval state | Is the package ready for qualified human communications review? |

Agents support professional judgment. They do not replace authorized spokespeople, communications leaders, journalists, legal counsel, privacy specialists, crisis teams, executives, regulators, or public authorities.

## Repository structure

```text
AGENTS/
├── research_agent.py
├── narrative_agent.py
├── stakeholder_agent.py
├── risk_agent.py
└── review_agent.py

SKILLS/
├── evidence_discipline.py
├── narrative_reasoning.py
├── stakeholder_reasoning.py
├── risk_reasoning.py
└── review_reasoning.py

TOOLS/
├── evidence_register.py
├── message_map.py
├── stakeholder_map.py
├── risk_register.py
└── review_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Evidence discipline

The policy requires `research_reviewed` and `evidence_provenance_reviewed`.

Communications should distinguish verified facts, attributed statements, estimates, interpretations, allegations, internal hypotheses, forecasts, and unknowns. F128 should not convert uncertainty into certainty for narrative convenience.

Material evidence should preserve source, date, owner, context, version, limitations, and review state. `evidence_provenance_gap` blocks release.

## Source hierarchy

Source quality depends on the subject. Primary records, authorized internal records, official statements, direct evidence, peer-reviewed research, regulatory material, and reliable contemporaneous reporting may carry different evidentiary weight.

The system should preserve disagreements between credible sources rather than silently choosing the most convenient version.

## Chronology

For incidents, launches, disputes, crises, and investigations, chronology is often critical. F128 can structure an event timeline while distinguishing event time, discovery time, reporting time, decision time, and publication time.

## Narrative architecture

The policy requires `narrative_reviewed`.

A narrative can include context, central message, supporting facts, proof points, stakeholder relevance, limitations, response options, and anticipated questions. Narrative coherence must never override factual accuracy.

## Message maps

`TOOLS/message_map.py` provides a deterministic surface for organizing core messages, evidence, audience variants, caveats, Q&A, and approval state.

A useful message map can preserve:

```text
message_id
audience
core_message
supporting_evidence
claim_status
caveats
spokesperson
channel
review_owner
approval_state
```

## Claims substantiation

The policy requires `claims_reviewed`.

`unsupported_claim` blocks release when a public statement exceeds reviewed evidence. F128 must never fabricate statistics, quotations, customer reactions, endorsements, partnerships, awards, research findings, media coverage, regulatory status, timelines, or outcomes.

## Attribution and quotation

Quotes should preserve speaker identity, authorization, wording, context, and approval where required. The system should not invent quotations or convert an internal draft into an attributed public statement.

## Spokesperson authority

`impersonation_risk` blocks release when identity, attribution, or spokesperson authority is unresolved.

Drafting support does not authorize the system to speak as an executive, employee, customer, expert, government official, journalist, or organization.

## Stakeholder mapping

The policy requires `stakeholder_reviewed`.

`TOOLS/stakeholder_map.py` can organize affected groups by information need, impact, relationship, urgency, channel, owner, and escalation requirement.

Stakeholders can include employees, customers, partners, investors, communities, journalists, regulators, policymakers, suppliers, creators, researchers, advocacy groups, and the public.

## Stakeholder sequencing

Communication order can matter. Employees, directly affected people, regulators, customers, partners, or other groups may require communication before or alongside public release.

F128 should surface sequencing conflicts rather than assuming public-first communication is always appropriate.

## Media relations

The system can research outlets, beats, publicly available journalist interests, publication context, and potential relevance. It can draft media materials and outreach options but cannot autonomously contact journalists.

`send_media_outreach` is a protected action.

## Media lists

Media lists should be relevant, current, respectful, and based on legitimate professional information. F128 should not scrape or expose private contact information or recommend indiscriminate mass outreach.

## Pitches

A pitch should accurately represent the news value and avoid deceptive personalization, fake familiarity, fabricated exclusivity, false urgency, or misleading claims about prior interest.

`deceptive_outreach` blocks release.

## Press releases

F128 can prepare press-release drafts with headline, dateline, factual body, quotations, boilerplate, media contact placeholders, and supporting links. `issue_press_release` remains protected and requires human-controlled execution.

## Embargoes

Embargoed information should preserve recipient scope, terms, timing, confidentiality, authorization, and release conditions. An embargo is not a substitute for a binding confidentiality agreement.

`privacy_confidentiality_gap` blocks release when embargo or confidentiality status is unresolved.

## Exclusives

Exclusive arrangements can affect fairness, sequencing, expectations, and relationships with other media. F128 can model options but should not promise exclusivity without authorization.

## Background and off-record boundaries

Terms such as on the record, background, deep background, and off the record can be interpreted differently across organizations and journalists. F128 should not assume a universal definition. Authorized humans should explicitly establish terms before sensitive conversations.

## On-record authority

`respond_on_record` is protected. The system cannot autonomously provide attributed public responses, even when a draft has passed internal review.

## Q&A preparation

F128 can prepare anticipated questions, evidence-backed answers, bridging options, caveats, unknowns, and escalation triggers. Q&A preparation should include difficult questions rather than only favorable ones.

## Interviews

Interview preparation can include objectives, audience, likely questions, factual boundaries, sensitive topics, bridging, supporting evidence, and follow-up obligations. The system cannot participate as the authorized spokesperson.

## Executive communications

Executive statements can create legal, financial, employment, regulatory, and reputational consequences. Drafts should preserve the executive's actual position and authority rather than manufacturing personal beliefs or commitments.

## Internal communications

Internal messages can include organizational changes, incidents, policy updates, launches, employee guidance, and leadership communications. Internal status does not eliminate confidentiality, employment, privacy, or factual risks.

## Employee communications

Employees should receive material information through authorized channels appropriate to the situation. F128 should not fabricate employee sentiment or represent coordinated internal messaging as spontaneous employee opinion.

## Customer communications

Customer messages should preserve product truth, service impact, timing, support paths, remedies, uncertainty, and applicable legal requirements. A communications objective should not hide material customer impact.

## Investor and financial communications

Communications involving financial performance, forecasts, fundraising, securities, material corporate events, or investor information can require specialized legal and finance review. F128 should not determine materiality or disclosure obligations autonomously.

## Regulatory communications

Responses to regulators or public authorities can create binding obligations. F128 can organize evidence and draft options, but authorized legal, compliance, executive, or regulatory professionals retain submission authority.

## Crisis communications

`crisis_escalation_required` blocks ordinary release when a crisis or material incident requires authorized escalation.

Potential crisis contexts include safety incidents, cybersecurity events, data breaches, product recalls, litigation, executive misconduct allegations, workplace incidents, public emergencies, misinformation waves, operational outages, regulatory investigations, or rapidly escalating reputational events.

## Crisis command structure

A crisis workflow should identify incident owner, communications lead, legal lead, operational lead, executive authority, subject-matter experts, affected stakeholders, decision cadence, approved channels, and escalation paths.

F128 supports this structure but does not become the incident commander.

## Holding statements

A holding statement can acknowledge a developing situation while facts are still being verified. It should avoid speculation, false reassurance, unsupported causation, or promises that cannot be kept.

## Speed versus accuracy

Rapid response can matter, but speed does not justify fabrication. F128 should explicitly surface unknowns and propose update cadence when facts are incomplete.

## Corrections

When a material public statement is wrong, correction planning should consider factual significance, affected audiences, distribution channels, legal requirements, timing, discoverability, and trust.

The system can draft a correction but cannot autonomously publish it.

## Retractions

Retractions can carry significant legal and reputational consequences. F128 can organize the evidence and communication options but should escalate final decisions to qualified humans.

## Apologies

An apology can involve responsibility, empathy, legal exposure, remediation, and future commitments. F128 should not fabricate accountability or admit legal liability without authorized review.

## Misinformation and rumors

The system should distinguish false claims, unverified claims, disputed claims, satire, opinion, misunderstanding, and incomplete reporting. It should avoid amplifying a rumor unnecessarily while preparing evidence-backed response options.

## Disinformation and coordinated manipulation

Potential coordinated manipulation should be treated as an evidence and escalation problem. F128 should not retaliate through deceptive amplification, fake accounts, harassment, or manufactured consensus.

## Social media communications

Social channels can accelerate both reach and risk. Public replies, posts, threads, videos, and executive social statements should preserve the same factual, privacy, legal, and authority standards as other external communications.

## Privacy

The policy requires `privacy_confidentiality_reviewed`.

Communications can expose names, health information, locations, customer details, employee information, private correspondence, incident details, children, or other personal data. Information should be minimized to what is legitimately needed.

## Confidential information

Unreleased financial information, product plans, security details, customer records, legal strategy, credentials, internal investigations, personnel matters, contractual information, and private communications should not be exposed without authorization.

## Legal risk

`legal_reputation_risk` blocks release when material legal or reputational risk remains unresolved.

Relevant areas can include defamation, privacy, intellectual property, securities, employment, advertising, consumer protection, confidentiality, contractual obligations, litigation, and regulatory requirements.

F128 does not provide legal approval.

## Defamation risk

Statements about identifiable people or organizations can create significant risk when allegations are unverified or framed as established fact. The system should preserve attribution, evidence status, uncertainty, and legal escalation.

## Intellectual property

Press materials can contain photographs, logos, charts, video, music, excerpts, research, trademarks, or third-party materials. Public availability does not establish reuse rights.

## Stakeholder harm

`stakeholder_harm_risk` blocks release when communication could create unresolved material harm to affected people or communities.

Risk review should consider privacy, safety, stigma, retaliation, discrimination, harassment, misinformation amplification, and disproportionate burden.

## Vulnerable people

Communications involving children, patients, victims, grieving families, people in crisis, or other vulnerable individuals require heightened dignity, consent, privacy, and safeguarding review.

## Accessibility

Public communications should consider captions, transcripts, alt text, readable documents, clear language, accessible web destinations, and inclusive formats.

## Inclusion and representation

Communications should avoid tokenism, stereotypes, fabricated representation, or using individuals as symbolic proof without consent. Representation claims should be grounded in actual organizational practice.

## Localization

Localization should preserve facts, legal meaning, cultural context, names, titles, units, dates, required disclosures, and tone. Literal translation alone can create material errors.

## International communications

Cross-border communication can involve different media systems, legal rules, political contexts, cultural expectations, privacy standards, and regulatory requirements. Local qualified review may be necessary.

## Political and public-policy communications

Policy, election, lobbying, and political communications can involve specialized legal, disclosure, factual, and organizational requirements. F128 should escalate these contexts rather than treating them as ordinary brand messaging.

## Public-sector communications

Government and public-sector communications can involve public records, accessibility, procurement, emergency information, statutory duties, neutrality, and records retention. Authorized public officials retain publication authority.

## Scientific and technical communications

Research claims should preserve study design, population, limitations, uncertainty, peer-review status, conflicts, and distinction between preliminary and established findings.

F128 should not turn a technical result into a stronger public claim than the evidence supports.

## Health communications

Health-related communications can affect patient behavior and public safety. Claims should be reviewed by qualified subject-matter and regulatory professionals when appropriate.

## Security incidents

Cybersecurity and data-breach communications should coordinate with incident response, legal, privacy, security, insurance, regulators, and affected parties as appropriate. Premature disclosure can create additional harm, while delayed disclosure can also carry obligations.

## Litigation communications

Active litigation and investigations require specialized legal control. F128 can organize public facts and draft options but cannot determine litigation strategy or waive privilege.

## Reputation monitoring

Monitoring can identify media coverage, public questions, stakeholder concerns, misinformation, and emerging issues. Visibility does not equal representativeness, and sentiment should not be treated as a precise measure of public opinion.

## Sentiment and media analysis

Coverage volume, tone, prominence, message pull-through, share of voice, journalist reach, and stakeholder response can support evaluation. Automated sentiment should preserve uncertainty, especially with irony, technical subjects, multilingual content, or polarized topics.

## Measurement

Communications measurement should connect activity to objectives. Potential indicators include message accuracy, reach, qualified coverage, stakeholder understanding, response time, correction rate, share of relevant conversation, inbound interest, trust measures, and downstream outcomes.

## Attribution limits

PR outcomes are influenced by news cycles, product quality, executive behavior, market events, paid media, social activity, customer experience, and many other factors. F128 should avoid claiming causal impact from simple before-and-after correlations.

## Media value equivalents

Advertising value equivalency can misrepresent earned media value. F128 should favor measures tied to actual communications objectives and evidence rather than automatically translating coverage into hypothetical ad spend.

## Reputation forecasting

Reputational scenarios are uncertain. The system can identify plausible consequences and sensitivities but should not present a predicted media response as guaranteed.

## Scenario planning

Risk analysis can model best case, expected case, adverse case, escalation triggers, stakeholder reactions, information gaps, and response options. Scenario planning should preserve uncertainty rather than create false precision.

## Risk register

`TOOLS/risk_register.py` provides a deterministic surface for issue, likelihood, impact, evidence, owner, mitigation, escalation, and status.

Material unresolved risks should remain visible through review rather than disappearing from a polished narrative.

## Change control

Facts, drafts, spokesperson assignments, stakeholder maps, embargo dates, media lists, legal guidance, and incident status can change rapidly. Material changes should trigger renewed review.

## Versioning

Public statements should have clear versions and approval state. Teams should be able to determine which wording was approved, when, by whom, and for which channel.

## Records and retention

Organizations may have records obligations for communications, approvals, press materials, incident documentation, and regulator interactions. F128 should support traceability without defining organization-specific retention law.

## Memory and state

The `memory/` layer can preserve structured workflow state across agents. It should distinguish verified evidence, drafts, allegations, private information, risk decisions, approvals, and published outcomes.

Sensitive information should be minimized and governed according to legitimate operational needs.

## Observability

The `observability/` layer supports traceability across evidence, narrative, stakeholder, risk, approval, and governance states.

Useful telemetry includes source state, claim state, draft version, stakeholder sequence, confidentiality state, risk severity, escalation state, approval state, and protected-action attempts.

## Required reviews

The executable policy requires all eight conditions:

```text
research_reviewed
narrative_reviewed
stakeholder_reviewed
risk_reviewed
claims_reviewed
privacy_confidentiality_reviewed
evidence_provenance_reviewed
qualified_communications_approval
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- a public claim exceeds reviewed evidence
- identity, attribution, or spokesperson authority is unresolved
- deceptive media or stakeholder outreach is detected
- privacy, consent, embargo, or confidentiality review is incomplete
- legal, defamation, or reputational risk remains unresolved
- a crisis or material incident requires authorized escalation
- material stakeholder-harm risk remains unresolved
- evidence provenance is incomplete
- any required review is missing
- qualified communications approval is missing

The system exposes blockers rather than manufacturing approval.

## Protected actions

The safety policy permanently protects:

```text
publish_statement
send_media_outreach
issue_press_release
respond_on_record
activate_crisis_response
external_distribution
```

These actions remain outside autonomous authority even after all required reviews are satisfied.

## Human authority boundaries

F128 must not autonomously publish statements, contact journalists, issue press releases, speak on the record, activate crisis communications, distribute external messaging, impersonate spokespeople, disclose confidential information, approve legal risk, or represent unverified allegations as facts.

Authorized humans retain control over public statements, media relations, crisis response, spokesperson authority, regulatory communications, legal positions, and binding external representations.

## Explicit failure states

```text
RESEARCH REVIEW REQUIRED
NARRATIVE REVIEW REQUIRED
STAKEHOLDER REVIEW REQUIRED
RISK REVIEW REQUIRED
CLAIM UNSUPPORTED
SPOKESPERSON AUTHORITY UNRESOLVED
DECEPTIVE OUTREACH DETECTED
PRIVACY OR CONFIDENTIALITY GAP
LEGAL OR REPUTATION RISK
CRISIS ESCALATION REQUIRED
STAKEHOLDER HARM RISK
EVIDENCE PROVENANCE GAP
QUALIFIED COMMUNICATIONS APPROVAL REQUIRED
PUBLICATION PROHIBITED
MEDIA OUTREACH PROHIBITED
PRESS RELEASE ISSUANCE PROHIBITED
ON-RECORD RESPONSE PROHIBITED
AUTONOMOUS CRISIS ACTIVATION PROHIBITED
EXTERNAL DISTRIBUTION PROHIBITED
```

## End-to-end reference workflow

1. Define the communication objective, context, authority, and affected stakeholders.
2. Build the evidence register and distinguish verified facts from unknowns and allegations.
3. Establish chronology when timing is material.
4. Develop narrative and message-map options grounded in evidence.
5. Map stakeholders, channels, sequencing, and spokesperson authority.
6. Prepare media, internal, customer, executive, or other communication options as appropriate.
7. Review claims, attribution, privacy, confidentiality, embargoes, and intellectual property.
8. Review legal, reputational, stakeholder-harm, misinformation, and crisis risks.
9. Preserve evidence provenance, draft versions, and unresolved uncertainty.
10. Apply fail-closed governance.
11. Require explicit qualified-human communications approval.
12. Keep publication, media outreach, press release issuance, on-record responses, crisis activation, and external distribution outside autonomous authority.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test evidence quality, narrative fidelity, stakeholder reasoning, risk detection, uncertainty handling, crisis escalation, and governance behavior.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, approved support release, unsupported claims, impersonation, deceptive outreach, confidentiality gaps, legal or reputation risk, crisis escalation, stakeholder harm, and provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed behavior, held-out governance scenarios, and execution of the governed reference workflow.

## Reproducibility

Reproducible communications analysis requires preserving sources, chronology, draft versions, claims, stakeholder maps, risk decisions, confidentiality state, spokesperson authority, approvals, and publication context.

## Extension points

Organization-specific implementations can add governed integrations for media databases, monitoring systems, document repositories, analytics, approval workflows, news feeds, incident-management systems, CRM, press rooms, and distribution platforms.

Any integration capable of contacting external parties or publishing content should remain behind explicit authorization, least privilege, audit logging, and human-controlled execution.

## Example applications

Potential governed uses include press-release drafting, media briefing preparation, executive communications, stakeholder mapping, crisis scenario planning, issue response, Q&A preparation, internal communications, launch communications, scientific communications, media analysis, and reputation-risk review.

F128 is not an autonomous spokesperson, journalist outreach bot, crisis commander, legal authority, regulator, or substitute for qualified communications judgment.

## Design principles

1. Facts before narrative convenience.
2. Preserve uncertainty, attribution, chronology, and evidence provenance.
3. Never fabricate quotes, coverage, endorsements, reactions, or authority.
4. Protect privacy, confidentiality, vulnerable stakeholders, and media relationships.
5. Escalate legal, reputational, crisis, and stakeholder-harm risks.
6. Separate drafting assistance from spokesperson authority.
7. Measure communication against objectives with explicit attribution limits.
8. Fail closed when material evidence or review is incomplete.
9. Keep all binding external communication under authorized human control.

## Scope statement

F128 demonstrates a governed multi-agent architecture for PR and communications decision support. It combines specialized research, narrative, stakeholder, risk, and review agents with deterministic evidence, message, stakeholder, risk, and review tools, observability, held-out evaluation, and fail-closed governance while preserving strict human authority over public communication and external outreach.

Author: Mahsa Keikha
