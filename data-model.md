# Data models

## Accounts microservice

---

### Accounts

| name             | type   | unique | optional |
| ---------------- | ------ | ------ | -------- |
| id               | int    | no    | no       |
| first_name       | string | no     | no       |
| last_name        | string | no     | no       |
| username         | string | no     | no       |
| password         | string | no    | no       |
| email            | string | no     | no       |

The `account` entity contains the data about a specific user
and theirinformation.

## Playlists microservice

---

### Playlists

| name             | type   | unique | optional |
| ---------------- | ------ | ------ | -------- |
| playlist_id      | int    | yes    | no       |
| name       | string | no     | no       |
| last_name        | string | no     | no       |
| username         | string | no     | no       |
| password         | string | no    | no       |
| email            | string | no     | no       |

### Questions

| name             | type   | unique | optional |
| ---------------- | ------ | ------ | -------- |
| question_1       | string | yes    | no       |
| question_2       | string | yes    | no       |
| question_3       | string | yes    | no       |
| question_4       | string | yes    | no       |
| question_5       | string | yes    | no       |
| question_6       | string | yes    | no       |
| question_7       | string | yes    | no       |
| question_8       | string | yes    | no       |
| question_9       | string | yes    | no       |
| question_10      | string | yes    | no       |

### Answers

| name             | type   | unique | optional |
| ---------------- | ------ | ------ | -------- |
| answer_1         | string | yes    | no       |
| answer_2         | string | yes    | no       |
| answer_3         | string | yes    | no       |
| answer_4         | string | yes    | no       |
| answer_5         | string | yes    | no       |
| answer_6         | string | yes    | no       |
| answer_7         | string | yes    | no       |
| answer_8         | string | yes    | no       |
| answer_9         | string | yes    | no       |
| answer_10        | string | yes    | no       |