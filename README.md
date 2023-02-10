![logo](/images/Disp_Logo_LG.png)

# Disposition
* Software Engineer: Thinh Mai
* Software Engineer: Merick
* Software Engineer: Lewey Melchor
* Software Engineer: Van Tu

---

## Intended Market

We are targeting general music consumers in the entertainment market who are looking for new music to listen to. Users of the application would find a wide array of popular music from different genres.

![Home page](/images/Home_page.png)

---

## Design

* [Wire Dragrams](wirediagram.md)
* [Data models](data-model.md)
* [APIs Endpoints](api.md)

---

## Functionality

- Visitors to the site can take a personality quiz pertaining to their specific mood by taking the Disposition's proprietary Vibe Check© quiz.
- Using advance algorithms, the results page will populate with playlist matching their personality quiz

- A top 10 page for a list view of the top 10 popular songs.

- A list of results all users got from the personality quiz

---

## Endpoints
- *Top 10 page*
  - moodz3.gitlab.io/disposition
- *User sign up page*
  - moodz3.gitlab.io/disposition/SignupForm
- *User login page*
  - moodz3.gitlab.io/disposition/Login
- *Vibe Check*
  - moodz3.gitlab.io/disposition/Vibecheck
- *History page*
  - moodz3.gitlab.io/disposition/history

---

## Project initialization
To fully enjoy this application on your local machine, please make sure to follow these steps:
1. Clone the repository down to your local machine
2. CD into the new project directory
3. Create the volume `docker volume create postgres-data`
4. Run `docker compose up`
5. Let us take you on a new musical carpet ride that will span generations! :smiley:
