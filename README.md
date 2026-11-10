# Horse Game iPad Runtime Build

Manual, pinned-source build of the experimental Madeira compatibility runtime
for iPad. This repository contains build instructions only: no game assets,
server code, account data, signing credentials or product keys.

## Build

Open **Actions → Build pinned iPad compatibility runtime → Run workflow**.
The workflow runs only when manually requested. Pushing files does not start
a build. It uses GitHub's standard Mac runners and uploads an IPA artifact;
it does not install or sign the app with an Apple account.

Every source checkout selects `willfaust/Madeira` at
`8b52c1810a0b77614238001ed86199978865afd1`. GitHub Actions implementations
are also pinned to full revisions in `action-pins.json`. Persisted checkout
credentials are disabled and the workflow token has read-only contents access.

The upstream component build and validation stages are preserved, including
i386 Wine and desktop OpenGL. Matching cached build outputs can be reused.
First builds may take hours and can fail on compiler, dependency or runner
resource constraints. No successful hosted build is claimed yet.

## Status

This is an experiment, not a ready-to-play iPad game. A successful build does
not establish runtime safety, game compatibility or playable performance.
Inspect the resulting artifact before installation. JIT, normal app signing,
graphics and the game-launch path still require device testing.

Standard hosted runners are free for public repositories according to
[GitHub's runner documentation](https://docs.github.com/en/actions/reference/runners/github-hosted-runners).
Private-repository usage is governed by the account's allowance and billing.

## Attribution

Adapted from [Madeira's build workflow](https://github.com/willfaust/Madeira/blob/8b52c1810a0b77614238001ed86199978865afd1/.github/workflows/build.yml).
Local adaptations: manual-only trigger, explicit source/revision pins at every
checkout, disabled persisted checkout credentials and pinned action revisions.
Runtime code is unchanged.

See `UPSTREAM-LICENSE` and `UPSTREAM-LICENSE-EXCEPTION.md` for upstream terms.
Madeira also uses separately licensed third-party components; see its
[build documentation](https://github.com/willfaust/Madeira/blob/8b52c1810a0b77614238001ed86199978865afd1/BUILDING.md)
and [security discussion](https://github.com/willfaust/Madeira/issues/583).
