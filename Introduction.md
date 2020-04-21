# Introduction

This playground describes my tooling and workflow for contests on CodinGame.
Some sections will use specific tools and programming languages but the concept can be adapted.

Reproducing a bug against a random opponent can be annoying. Even when the behaviour is perfectly reproducable online,
it can be hard to debug in the offline IDE, when a match history is needed. Some games like Ocean of Code deal with
fog of war, so copying the referee input of a single turn isn't enough to reproduce the same situtation offline.

Initially we will explore the CodinGame API to understand how to download replays.
Then we will parse them to extract the data we are looking for. We will then feed it into our bot to debug a specific action.
