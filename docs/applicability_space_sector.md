# Does NIS2 apply to a space / Earth-observation company?

This note answers the question a compliance team asks first: *do the new requirements apply to us?*
The answer for a space company is **"it depends on what the company does"**. Space is in NIS2, but the scope is narrower than the name suggests.

## 1. Three possible routes into NIS2

| Route | Where in NIS2 | What the company must do to be in scope | Category if in scope |
|---|---|---|---|
| Space sector | Annex I, sector 11 (high criticality) | Operate **ground-based infrastructure** that supports space-based services (ground stations, mission control, satellite data reception). Public electronic communications providers are excluded. | Essential if large, important if medium |
| Manufacturing | Annex II, "manufacture of other transport equipment" (NACE C30, includes spacecraft) and electronics (NACE C26) | Build satellites, spacecraft or electronic equipment | Important (if medium or large) |
| Digital / ICT services | Annex I, digital infrastructure and ICT service management | Provide data centre, cloud or managed ICT services to other companies | Essential or important depending on size |

Size test (Art. 2 + Art. 3): in general, NIS2 applies to **medium and large** companies. Medium = 50+ staff or more than EUR 10M turnover and balance sheet. Large = 250+ staff, or more than EUR 50M turnover and more than EUR 43M balance sheet.

A common mistake: "we build satellites, so we are in the space sector". Building satellites is manufacturing (Annex II), not Annex I space. Only the ground segment operator falls under the space sector.

## 2. Even if the company is not in scope

NIS2 also reaches suppliers. Art. 21(2)(d) obliges in-scope entities to manage supply-chain security, so their customers (e.g. a space agency or a ground-segment operator) will push security clauses into supplier contracts. An ISO 27001 certificate plus a NIS2 gap analysis is a strong answer to those questionnaires.

## 3. French status (regulatory watch, November 2026)

- France has not finished transposing NIS2. The deadline was 17 October 2024.
- The transposition law is the *projet de loi relatif à la résilience des infrastructures critiques et au renforcement de la cybersécurité* ("loi Résilience"). It also transposes the CER directive and adapts French law to DORA.
- Senate adopted it on 12 March 2025. The Assemblée nationale debated it on 9 and 10 November 2026 and scheduled the final vote (vote solennel) for 17 November 2026. A joint committee (CMP) then has to agree a single text before the law is promulgated.
- On 8 July 2026 the European Commission referred France to the EU Court of Justice for not transposing on time.
- ANSSI published the **ReCyF** (Référentiel Cyber France), version 2.5, on 17 March 2026. It lists the security objectives France will require (15 for important entities, 5 more for essential entities) and the measures ANSSI recommends to meet them. It is a working document and not mandatory by default, but an entity that applies it can rely on it during an ANSSI inspection.
- ANSSI also offers a comparison tool that maps ReCyF against other frameworks, including ISO 27001. **Next step for this project: check my mapping against that tool.**

## 4. To watch

- Final vote of the loi Résilience and the implementing decrees (décrets) that fix the exact list of entities.
- Final version of ReCyF after consultation.
- The proposed EU Space Act (Commission proposal, 2025), which would add cybersecurity rules specific to space operators.
