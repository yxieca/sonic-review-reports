# Current human-operated feedback drafts

Target: https://github.com/sonic-net/sonic-gnmi/pull/924
Reviewed HEAD: `bcdcf8a67fd425880fd1319bd0606b2007b2ebcd`
Report: https://github.com/yxieca/sonic-review-reports/pull/78

## Comment without a verdict

The checksum-only update at `bcdcf8a67fd425880fd1319bd0606b2007b2ebcd` resolves the previously raised native module-tidiness issue. Current `go.sum` equals the PR BASE version; no runtime or filename code changed. The existing Azure no-write tidy gate reports success, attributed externally.

**Nonblocking: preserve the selected temporary filename as data.** [getMixedDbWorkPath](https://github.com/sonic-net/sonic-gnmi/blob/bcdcf8a67fd425880fd1319bd0606b2007b2ebcd/sonic_data_client/mixed_db_client.go#L75-L81) still honors arbitrary nonempty process `TMPDIR`. [SetFullConfig](https://github.com/sonic-net/sonic-gnmi/blob/bcdcf8a67fd425880fd1319bd0606b2007b2ebcd/sonic_data_client/mixed_db_client.go#L1584-L1603) inserts the resulting path into [PyCodeForYang's double-quoted Python source literal](https://github.com/sonic-net/sonic-gnmi/blob/bcdcf8a67fd425880fd1319bd0606b2007b2ebcd/sonic_data_client/mixed_db_client.go#L1392-L1407) without escaping it. A legitimate directory name containing a double quote can produce invalid Python source; a backslash sequence can refer to a different filename. Please pass the filename separately as data or serialize a lossless quoted literal. This unchanged note was already included in the [submitted questions](https://github.com/sonic-net/sonic-gnmi/pull/924#issuecomment-7205039251); prefer continuing that discussion, not reposting it. The process environment is trusted here—no remote-execution or authentication vulnerability was reproduced. Prior AST-only filename controls were retained, not rerun as native Python/Go validation.

N1 remains nonblocking and was already raised in the existing questions; do not repeat that feedback. The target remains draft. Reviewer native imports, builds, Go/Bazel/compiler/test suites, Redis/gNMI/TLS/network payloads, installation and DUT/hardware checks were not run. Reviewed HEAD: `bcdcf8a67fd425880fd1319bd0606b2007b2ebcd`. Full report: https://github.com/yxieca/sonic-review-reports/pull/78.

## Source-favorable approval draft, manual and freshness-gated

The checksum-only update at `bcdcf8a67fd425880fd1319bd0606b2007b2ebcd` resolves the previously raised native module-tidiness issue. Current `go.sum` equals the PR BASE version; no runtime or filename code changed. The existing Azure no-write tidy gate reports success, attributed externally.

**Nonblocking: preserve the selected temporary filename as data.** [getMixedDbWorkPath](https://github.com/sonic-net/sonic-gnmi/blob/bcdcf8a67fd425880fd1319bd0606b2007b2ebcd/sonic_data_client/mixed_db_client.go#L75-L81) still honors arbitrary nonempty process `TMPDIR`. [SetFullConfig](https://github.com/sonic-net/sonic-gnmi/blob/bcdcf8a67fd425880fd1319bd0606b2007b2ebcd/sonic_data_client/mixed_db_client.go#L1584-L1603) inserts the resulting path into [PyCodeForYang's double-quoted Python source literal](https://github.com/sonic-net/sonic-gnmi/blob/bcdcf8a67fd425880fd1319bd0606b2007b2ebcd/sonic_data_client/mixed_db_client.go#L1392-L1407) without escaping it. A legitimate directory name containing a double quote can produce invalid Python source; a backslash sequence can refer to a different filename. Please pass the filename separately as data or serialize a lossless quoted literal. This unchanged note was already included in the [submitted questions](https://github.com/sonic-net/sonic-gnmi/pull/924#issuecomment-7205039251); prefer continuing that discussion, not reposting it. The process environment is trusted here—no remote-execution or authentication vulnerability was reproduced. Prior AST-only filename controls were retained, not rerun as native Python/Go validation.

N1 remains nonblocking and was already raised in the existing questions; do not repeat that feedback. The target remains draft. Reviewer native imports, builds, Go/Bazel/compiler/test suites, Redis/gNMI/TLS/network payloads, installation and DUT/hardware checks were not run. Reviewed HEAD: `bcdcf8a67fd425880fd1319bd0606b2007b2ebcd`. Full report: https://github.com/yxieca/sonic-review-reports/pull/78.

Source-favorable draft only: check current non-draft status, revision and integration gates before choosing a formal approval. This page does not submit or release those gates.

## Previous feedback

Questions7205039251werealready submitted at913d4ae3. Do not repeat the historical R1/N1 feedback or replay the processed decision.
