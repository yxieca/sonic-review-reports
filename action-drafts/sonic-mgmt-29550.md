# Reader drafts: sonic-mgmt #29550

Report: REPORT_PR_URL

## Comment

Source review supports the NTP/syslog polling correction. NTP now retries active AND newer process start, rather than active once followed by an immediate old timestamp failure. Syslog checks retry exact parsed server membership and rollback-set equality; the pinned show producer reads rendered rsyslog.conf, not only ConfigDB. These checks do not certify NTP synchronization, remote delivery or completion of every service lifecycle.

Nonblocking timeout diagnostics — show observed syslog servers. In tests/generic_config_updater/test_syslog.py::expect_res_success_syslog/check_syslog_servers_match, both mismatch warnings print expected_content_list rather than current_syslog_servers. A removal poll therefore reports an unexpected address “in []”, concealing the actual stale/configured state. Include the observed list in missing/forbidden-server warnings, optionally alongside expected and unexpected lists. This can follow separately; it changes diagnostics, not acceptance.

Reviewed HEAD:e8a6af88b51c52d007b3979f3ba68c78538ac2d0, BASE77f1be96df60f44c13f4fc2b683ab3b77de27e4f. Full three-independent-general plus separate-SME source review and coordinator grounding. Exact source predicates were checked with inert record hosts/fake wait loops, not DUT execution. No pytest/native import, Ansible/GCU/NTP/syslog/Redis/device/service operation. Current hosted Azure/static checks succeeded; individual executed test/image/dependency selection is not independently verified. Report: REPORT_PR_URL. Check current revision, CI and replies before submission.

## Approve

Source approval with a nonblocking diagnostic follow-up that can be handled separately.

Source review supports the NTP/syslog polling correction. NTP now retries active AND newer process start, rather than active once followed by an immediate old timestamp failure. Syslog checks retry exact parsed server membership and rollback-set equality; the pinned show producer reads rendered rsyslog.conf, not only ConfigDB. These checks do not certify NTP synchronization, remote delivery or completion of every service lifecycle.

Nonblocking timeout diagnostics — show observed syslog servers. In tests/generic_config_updater/test_syslog.py::expect_res_success_syslog/check_syslog_servers_match, both mismatch warnings print expected_content_list rather than current_syslog_servers. A removal poll therefore reports an unexpected address “in []”, concealing the actual stale/configured state. Include the observed list in missing/forbidden-server warnings, optionally alongside expected and unexpected lists. This can follow separately; it changes diagnostics, not acceptance.

Reviewed HEAD:e8a6af88b51c52d007b3979f3ba68c78538ac2d0, BASE77f1be96df60f44c13f4fc2b683ab3b77de27e4f. Full three-independent-general plus separate-SME source review and coordinator grounding. Exact source predicates were checked with inert record hosts/fake wait loops, not DUT execution. No pytest/native import, Ansible/GCU/NTP/syslog/Redis/device/service operation. Current hosted Azure/static checks succeeded; individual executed test/image/dependency selection is not independently verified. Report: REPORT_PR_URL. Check current revision, CI and replies before submission.
