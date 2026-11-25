# Human-operated feedback drafts

Report: https://github.com/yxieca/sonic-review-reports/pull/19
Reviewed SHA: `5240b3d4505534b82848a7b9c9e073be25663e4a`
Coverage: completed three independent general passes, separate SME and grounding.

## Questions

For reviewed SHA 5240b3d4505534b82848a7b9c9e073be25663e4a, could you clarify/fix ganged physical-member handling in the existing ganged-member thread (https://github.com/sonic-net/sonic-utilities/pull/5074#discussion_r4679055165)? The new DOM resolver requires one logical mapping; an active ganged port overlapping two static mappings raises before output, unlike the base physical-member reads.

Full batch review report: https://github.com/yxieca/sonic-review-reports/pull/19. Three independent general passes and the separate SME are complete. No hardware or firmware validation was executed. This is a question without approval or a formal verdict; check current head and replies and avoid duplicating already answered feedback.

## Request changes

At reviewed SHA 5240b3d4505534b82848a7b9c9e073be25663e4a, the full batch source review in https://github.com/yxieca/sonic-review-reports/pull/19 identifies R1: the new single-interface resolver can reject previously readable ganged physical entries. Please address the existing ganged-member thread (https://github.com/sonic-net/sonic-utilities/pull/5074#discussion_r4679055165), preserving ordinary bank reuse and adding a multi-static-interface ganged case with distinct physical members. This references existing feedback rather than adding a duplicate finding.

Three independent general passes and the separate SME are complete; no hardware or firmware validation was executed for this assessment. Check the current head, author replies and report before submitting. This draft does not assert anyone else's approval.
