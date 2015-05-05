## TDD Kata - FindAPerson

### Intro
In this homework we are exercising Test Driven Development.
In this method code is mostly written through the following cycle: Test (Red) -> Code (Green) -> Refactor.
We will also use git to document the process.

You can either follow the given problem or ask the course team for another problem, e.g.,  from the Kata page in the lecture slides.

### The Problem
Let's take a look at [Ushahidi](http://www.ushahidi.com/), which is a platform, services and tools for geographical crowd sourcing, e.g., for coordinating rescue eefforts following a natural crisis ([Nepal](http://www.ushahidi.com/2015/04/29/status-update-regarding-ushahidi-deployments-for-nepal/)).   The [Crowdmap - Basic Features](https://wiki.ushahidi.com/display/WIKI/Crowdmap+-+Basic+Features),  are:

* Create a post
* Create a Map
* Find Posts
* Find a Map
* Collaborate
* **Find a Person**: This feature will be added at a later date. Stay Tuned
* See all the latest Posts
* See all the latest photos
* Map view
* View a post by Location

![](https://wiki.ushahidi.com/download/attachments/8356261/View%20a%20post%20from%20a%20location.png?version=1&modificationDate=1367443180000&api=v2&effects=border-simple,blur-border,tape)

Since there is a missing feature we are going to implement it!

Feature: Find a Person!
* Given a person name, return all posts (of a map) containing it’s name (in any of a post fields)
* Given a name, check if the map includes a location information (place or geo. location)
* Check if there are map inconsistencies, e.g., the same name with different locations.
Example: Or (R.I.P) appears at [27°59′N 86°55′E] but also at [31°47′N 35°13′E]

### Work Instructions
1. To start, [**fork** the exercise repository][forking] (or [pull][ref-pull] for later updates: ```git pull upstream master```).
1. [**Clone**][ref-clone] the repository to your computer.
1. Modify/add files (in the repository directory) and [**commit**][ref-commit] changes to complete your solution.
    * Each TDD phase needs to be committed separately with a suitable message, e.g. “RED: Test for finding a name”.
    * If you do pair programming, you should switch roles between RED and GREEN (see [here]( http://c2.com/cgi/wiki?PairProgrammingPingPongPattern), there is also a fun [Eclipse game]( http://www.happyprog.com/pairhero/) to guide it).
    * You can suggest other features by editing the requirements above.
1. [**Push**][ref-push]/sync the changes up to GitHub.
1. [Create a **pull request**][pull-request] to the original repository to turn in the assignment, don't forget to mention your pair.

A pull-request screencast [demo](http://screencast-o-matic.com/watch/coe3IEeMDa) (done for another course)

### Dates
Submit a pull request by next Tirgul (this time you don’t need to use the regular submitting form, but you can if you must :smile:).
We will give feedback through the pull-request system.
Good luck!

<!-- Links -->
[forking]: https://guides.github.com/activities/forking/
[ref-clone]: http://gitref.org/creating/#clone
[ref-commit]: http://gitref.org/basic/#commit
[ref-push]: http://gitref.org/remotes/#push
[ref-pull]: http://gitref.org/remotes/#pull
[pull-request]: https://help.github.com/articles/creating-a-pull-request
