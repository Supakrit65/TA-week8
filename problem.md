# Problem: Bag of Holding V1

There are two sets of instructions on separate matters. You must do them both.

## Git Repository Instructions

You must do the following:

* You must continue developing the code, creating at least two more commits on
  top of the template code given.
* The commit pointed by the HEAD tag must contain both files listed below.
* There must be a README.md file, containing your email address, your full name,
  and your student ID number, one per line.
  * This email address must be the same as the one used in GitHub Classroom.
    (It does NOT have to be your ku.th address!)
  * Your full name must use the spelling as indicated in Google Classroom.
  * Any other comments beyond the third line are ignored.
* The file to be graded MUST be called "bag.py".
* Any files provided by the lecturer can be left in, but they will be ignored.

Example README.md file:

```
Kasetsart STUDENT 
kasetsart.st@gmail.com
6500000000

Any other comment goes here...
```

To configure your username and email in the Git environment, from your command
line tool, use the following commands:

```
git config user.name "Kaset BRILLIANCE"
git config user.email "kaset.br@gmail.com"
```

This changes your Git username and email just for this repository.

You can use `git config --global ...` instead to make the commands affect
every single repo onwards.

## Programming Problem Instructions

See the bag.py file. You are required to implement an item container system for
a role-playing game. This container, called a Bag of Holding, or simply a Bag,
accepts only items with unique names (items with similar names are rejected),
each with a weight that can be any real number from 0 to 10,000.

The Bag, at this moment, has neither weight nor size limit. However, the SIMPLE
test will not add more than 10,000 items. The CHALLENGE test will ensure that
there are no more than 10,000 items at a time. The MONSTER test will ensure
there will be at least 10,000,000 items added, there will be repeated weight
queries, and there will be many deliberate attempts to trigger errors in your
code outside those formally documented. The time taken to run the MONSTER test
must not exceed 1500x the time taken to run the CHALLENGE test or it will fail.

Since the Bag opens to the Astral Plane, adding a Bag into another Bag is not
permitted. To prevent mishaps, a Bag should just reject anything that says "bag"
case-insensitively, so that includes "bAg" or "BAG", etc., as well.

Item names are strings only and are case-sensitive. For example, a "Sword" is a
different item from a "swOrd". The only permitted characters in an item name
include all printable characters from the ASCII character set.

At this moment, any operation that is illegal should be ignored. For example,
if you try to add a duplicate item, the bag should reject it.

Also, please fix my PEP 8 violations.

*For D&D Players: do not assume the Bag in this problem is the same as in D&D.*

## What is the Bag?

The Bag is, well, a bag. It does have a real-number weight.

Adventurers may add an item to the Bag, specifying its name and weight.
They may also remove an item, but they have to know its name. The total
weight may be queried directly. The items inside can be listed, but the
weight of each item remains a mystery. Finally, all the items inside
can be dumped out of the bag all at once, in which case it will be
returned as a list of tuples.

Additionally, some savvy craftsmen have created methods to add and remove
many items at a time. This may prove necessary if you want to defeat a
particularly strong MONSTER.

The Bag class must expose the following methods:

* `__init__`
* `add`
* `remove`
* `weight`
* `items`
* `dump`

If you want to complete the MONSTER test, you must also implement:

* `addmany`
* `removemany`

The description of each method is provided in the sample file.

You may develop directly from the sample file, which is given not as a gift,
but as a constraint.

You may create additional methods as needed, but in my experience I find that
the methods provided are enough.

## Testing

All items will be tested using a dedicated Python script. The SIMPLE test has
the same standards and rigors as the provided doctest, so if you pass the
doctest then you should get full marks on SIMPLE, at least for the programming
part.

The SIMPLE test is required to pass. CHALLENGE and MONSTER levels are optional
but of course will enhance your class experience.

The SIMPLE test is available in plain text script test_simple.py. The CHALLENGE
and MONSTER tests are obfuscated (you cannot see the source).

The obfuscated tests are difficult to develop and will be given to you later.

## Grading Rules

```
1. [ 5] The submission is a valid git repository.
2. [ 5] Git repo has the correct branch name ("master" XOR "main").
3. .... Files in the repo: 
   [ 5] The directory contains "README.md", "bag.py", and ".git" (repo data)
   [ 5] The files are named correctly, with the correct cases.
   [ 5] No other files, except those given by the lecturer, are included in
        the repository.
4. .... README.md
   [ 5] The file contains the full name.
   [ 5] The file contains the email address.
   [ 5] The file contains the student ID.
   [ 5] The order of the lines is correct.
5. .... bag.py
   [ 5] The Bag class has the correct methods and nothing extraneous.
   [ 5] The Bag class has the correct attributes and nothing extraneous.
   [ 5] The Bag.__init__ method is implemented correctly.
   [ 5] The Bag.add method is implemented correctly.
   [ 5] The Bag.remove method is implemented correctly.
   [ 5] The Bag.weight method is implemented correctly.
   [ 2] The Bag.items method is implemented correctly.
   [ 3] The Bag.dump method is implemented correctly.
   [ 5] No PEP 8 violations.
6. .... Repository state
   [10] The repo contains at least one commit made by you, using the same
        user name and email address as written in the README.md file.
   [ 5] The working area must be empty. (All files completely committed.)
```

> Maximum mandatory credit: 100.

```
8.  [20] Pass the CHALLENGE test.
9.  [10] The Bag.addmany method is implemented correctly.
10. [10] The Bag.removemany method is implemented correctly.
11. .... Pass the MONSTER test.
    [10] Program did not crash after adding 10+ million items.
    [10] Secret Error 1 avoided
    [10] Secret Error 2 avoided
    [10] Secret Error 3 avoided
    [10] Secret Error 4 avoided
    [10] Performance criteria: MONSTER test completed within 1500x time for
         CHALLENGE test
```

> Maximum optional credit: 100.

```
12. [20] Be the first to finish the MONSTER test.
13. [20] Be the first to submit work that avoids Secret Error 1.
14. [20] Be the first to submit work that avoids Secret Error 2.
15. [20] Be the first to submit work that avoids Secret Error 3.
16. [20] Be the first to submit work that avoids Secret Error 4.
```

> Maximum competition credit: 100.

Scoring for the competition credit, for each point, is as follows:
[20, 15, 12, 10, 9, 8, 7, 6, 5, ...]

You cannot earn any optional credit without maxing out the mandatory credit.
You cannot earn any competition credit without maxing out the optional credit.

Scores above 100 are treated as 100 for official evaluation purposes. I'll tell
you what happens with extra score later, but it's a good idea to earn as much as
you can.

Timing is based on the final submission. Therefore, if you have completed all
your work, you should stop pushing any more code.

## Specific Conditions

* You may use `math` or `itertools` if required. You may not import anything
  else, especially `os` or `sys`. (NG)
* Your code may not create external network connections. (NG)
* Your code may not open a file. (NG)
* Your code may not create additional threads. (NG)
* Late submissions are penalized. (-20 points penalty per day)
* Items marked NG means work will "Not be Graded" if you violate them.
* Extraneous means not meaningfully used.

Penalized work cannot obtain any sort of extra credit.

## Notes

* Please keep this repository intact as it will continue to be used later.
* Failure to do so may require you to repeat work.
* Copying code from a classmate or online sources counts as plagiarism and
  will be met with disciplinary action. If you lose your code, you need to
  rewrite it yourself.

Errors in critical areas such as (1), (2), and (3) may prevent correct
grading and may prevent the student from obtaining any score at all.

All grading rules are enforced by an automatic script. However, deliberate
attempts to spoil the intentions of the problem by exploiting the capabilities
(or lack thereof) of the automatic grading system ("cheesing") will be given
zero points. Disciplinary actions may be taken if such behavior is also
considered intentional and/or disruptive.

# Hints

* You may implement Bag using a list, a dict, or some other data structure as
  long as you expose the same methods that share the same outward behavior.
* There are many tricks that you can use to improve the performance of your
  program. Try to avoid going into loops when possible. (You'll learn more in
  later courses.)
* There are 4 secret errors that will be part of the MONSTER test. You will be
  told only when you fail them. The only hint is that you must read your
  assignment statement carefully.
* This is not the same kind of test that you've always been doing in the elab
  environment. In this exercise, your API is directly tested using a dedicated
  script.
* Commit often. Commit every time you make something and it works.

