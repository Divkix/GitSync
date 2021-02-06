# GitSync

![Sync Git Repos](https://github.com/Divkix/GitSync/workflows/Sync%20Git%20Repos/badge.svg)

A simple github action to sync all you public github repositories to gitlab!

### Currently Supports:
- [Gitlab](https://gitlab.com)

## Setup

### Setup Github Secrets
A guide to set Github Secrets can be found here:
https://docs.github.com/en/actions/reference/encrypted-secrets

You can set Secrets from you Github Project Settings.

You need to set these 2 Secrets:
- GitHubAccessToken
	A guide can be found here: [Creating a personal access token - GitHub Docs](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
- GitLabAccessToken
	A guide can be found here: [Personal access tokens - GitLab Docs](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html)


This action runs once every day.
You can even run it manually by going to Actions Tab and then clicking Run Workflow
