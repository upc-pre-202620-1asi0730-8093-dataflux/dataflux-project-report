# Reference diagram review

The original product architecture is the baseline, not the current mock implementation. Reference images from commit 75c2de8 are unchanged; the current develop 2b03cfc README confirms the seven complete backend class views. PlantUML source was recovered from PNG metadata rather than reconstructed from screenshots.

## Decisions and evidence

| Change | Decision | Evidence / reason |
|---|---|---|
| Six business contexts and Shared support | Preserve | Reference C4 context/component IDs and backend class packages are retained. Shared is technical support. |
| Interfaces, Application, Domain, Infrastructure | Preserve | All six reference class diagrams already express these layers, repository abstractions and adapters. |
| Replace backend UML with current JavaScript entities | Reverse | Section 4.7 describes product design. The statement does not require deleting a proposed backend class because TB1 has only a mock. Current JavaScript diagrams remain supplementary. |
| Remove RentalContract, ProviderProfile, MaintenanceRecord or payment ports | Reverse | These are present in the reference domain design. Their absence from the TB1 implementation does not invalidate the proposal. |
| Remove administrator, Maps, Stripe or SendGrid from C4 | Reverse | Restore their planned scope; do not claim implementation or deployment in TB1. |
| Angular / Spring / JPA / PostgreSQL labels | Adapt | The statement and project use Vue/JavaScript and proposed C#/ASP.NET Core/EF Core/MySQL. One original container diagram already used this stack while other views retained old labels. |
| Java primitive/date types and JPA repository fields | Adapt | Use C# types and DbContext in the same declared classes and layers; preserve class names, operations and relationship topology. |
| Backend context zoom labelled as a separate container | Clarify scope label | Keep the same boundary and component graph; label it as a detail of the one RESTful API. C4 containers are independent deployment units (statement page 19). |
| API drawn as a database in the frontend overview | Correct symbol | C4 distinguishes an independently deployed API container from its database; alias and relationships remain unchanged. |
| Split database design into six context views | Retain | Statement pages 19–20 require database diagrams per bounded context. Views use the original domain tables rather than substitute the mock DTO schema. |
| FK and optional cardinality consistency | Correct explicitly | ProviderProfileId resolves to provider_profiles; pending requests and not-yet-delivered contracts allow zero-or-one children. Optional MaintenanceRecord/Incident association uses nullable unique incident_id, preserving the class diagram. These are consistency corrections, not stack-only edits. |

## Reproducible validation

`reference-validation.json` records recovered source hashes, original class names, C4 element IDs and relation counts. Declaration names and relationship topology are preserved for the 26 adapted C4/UML models. The seven database views share one set of original tables and explicit foreign-key relationships. Original images are not overwritten. Four frontend images lack recoverable PlantUML metadata; their original files remain available as reference and are not represented as newly recovered sources.

The statement distinguishes software design from implemented release evidence. C4 requires context, independent deployment containers and component responsibilities/technology; UML requires context-level classes, members and relations; ERD requires columns, keys and relations. Those requirements justify clear proposal/runtime labels and complete relational views, not replacing the original DDD architecture with the current demo's smaller class set.
