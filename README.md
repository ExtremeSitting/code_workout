# code_workout

The goal of this project is to provide ever-changing and difficult challenges to improve code comprehension. All of the challenges assume you'll be writing your answers in bash, but you can use any language. Ideally you'll use a language that you're not comfortable in and gain skill in that language as you do more challenges.

I'll provide resource scripts in any language that feels right or is convenient. I don't write the challenges with a solution in mind or work out a solution to provide users. All of the challenges are possible, but may have long or ugly answers. It's not important that you have an elegant solution. **If it looks dumb, but it works; it's not dumb.**

## workout_notes

* **Saturday.** I intend to provide new challenges every Saturday night. If I miss a Saturday, I'll catch up the following day.
* **This should challenge you.** I intend to provide challenges that are possible, but difficult. Most challenges will start easy, or have easy goals, but the difficulty should escalate quickly. If you find the challenges too easy then you may want to choose a language you aren't as comfortable with or maybe you're just too good.
* **Goals are unordered.** The goals are presented in the order that I first thought of them. Feel free to jump around.
* **For the bold.** Some challenges will include a *bonus* section. This section is inteded to challenge those who found the other goals easy or just want more.
* **Text manipulation.** A lot of challenges may deal with general text manipulation. I find that a lot of administrative tasks fall in this category, but don't be fooled. You can easily take the lessons learned here and apply them in a different way to fit a more *real world* scenario for you.
* **BUGS!** If there are bugs in the resources (and you can provide proof), let me know by submitting an issue or maybe a pull request if you want to contribute.

## work_flow

* Fork this repo
* Create an *answers* branch
* Keep the master branch updated from upstream
* Merge *master* to *answers* so you can work out of the *answers* branch
* Do your work in the *answers* branch.

The answer branch is for you. You'll never be required to submit it or share it. I suggest keeping your notes and scripts in the weekly challenge directory. If you want to make changes to the resources, make a copy or you'll risk merge conflicts when you merge *master* to *answers*.

#### tools

The git-up script is a handy way to keep your fork and branches updated. You can drop it in /usr/local/bin/ (owned by root with executable permissions) and run it with like this:

```bash
$ git up
```

Make sure to add *upstream* as a remote:
```bash
$ git remote add upstream https://github.com/TheCodeWorkout/code_workout.git
```
If you want it to do a little more, you can un-comment the two lines at the bottom. When you run it, it will change to your answers branch and merge the changes from master.
