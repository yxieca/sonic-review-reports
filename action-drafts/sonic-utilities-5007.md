# Current reader drafts: sonic-utilities #5007

## Comment
Source corrections accepted: cpoutil/main.py::_interrupt_on_termination preserves inherited SIG_IGN and ignores recorded TERM/HUP signals during the first termination unwind; HUP-first detaches output before KeyboardInterrupt. _transfer_firmware closes its generator across download and the run/commit tail; the phase announcement precedes completion, and late errors retain bytes. Prior R1/N1/N2 fixes remain intact; do not repost them.

Optional signal hardening: handler installation/bookkeeping occurs before the restoration try/finally, so an interrupt during setup can leave a partial handler state; use transactional setup/restoration if strengthening that boundary. _detach_output can raise before KeyboardInterrupt or close FD1/2 if os.open reused an already closed standard descriptor; retain abort classification on redirection failure and close only a non-destination temporary FD. These extra preconditions were not reproduced and are not blocking device-failure claims. TERM-first/HUP-later and SIGINT orderings, plus output sites outside progress.update, remain qualification cases. Describe nohup as inherited ignored SIGHUP remaining ignored, not ordinary TERM immunity.

Q1 linked platform-common polling before commit is inspected at a pinned revision; image/endpoint selection and hardware verification remain separate. Do not treat a linked correction as deployed or repeat the acknowledged dependency question.

ReviewedHEAD:ba3451bfaabedf9ae3a5341033788a3cb710aea3. Original full panel and earlier increment preserved; new independent general/SME behavioral checks plus linked-hook source checks. No reviewer firmware/native/PTY/tests/device operations. Linked dependency source is not proof of image/endpoint installation or hardware outcome. Report: https://github.com/yxieca/sonic-review-reports/pull/18. Check current revision/replies/effective review state.

## Approve
Source approval within the reported contract; optional follow-ups can follow separately.

Source corrections accepted: cpoutil/main.py::_interrupt_on_termination preserves inherited SIG_IGN and ignores recorded TERM/HUP signals during the first termination unwind; HUP-first detaches output before KeyboardInterrupt. _transfer_firmware closes its generator across download and the run/commit tail; the phase announcement precedes completion, and late errors retain bytes. Prior R1/N1/N2 fixes remain intact; do not repost them.

Optional signal hardening: handler installation/bookkeeping occurs before the restoration try/finally, so an interrupt during setup can leave a partial handler state; use transactional setup/restoration if strengthening that boundary. _detach_output can raise before KeyboardInterrupt or close FD1/2 if os.open reused an already closed standard descriptor; retain abort classification on redirection failure and close only a non-destination temporary FD. These extra preconditions were not reproduced and are not blocking device-failure claims. TERM-first/HUP-later and SIGINT orderings, plus output sites outside progress.update, remain qualification cases. Describe nohup as inherited ignored SIGHUP remaining ignored, not ordinary TERM immunity.

Q1 linked platform-common polling before commit is inspected at a pinned revision; image/endpoint selection and hardware verification remain separate. Do not treat a linked correction as deployed or repeat the acknowledged dependency question.

ReviewedHEAD:ba3451bfaabedf9ae3a5341033788a3cb710aea3. Original full panel and earlier increment preserved; new independent general/SME behavioral checks plus linked-hook source checks. No reviewer firmware/native/PTY/tests/device operations. Linked dependency source is not proof of image/endpoint installation or hardware outcome. Report: https://github.com/yxieca/sonic-review-reports/pull/18. Check current revision/replies/effective review state.