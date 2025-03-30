# AI_Learning
My notes and projects on AI Learning.

Here I'll capture all work related to testing with Google AI


How to push to the repo:


USING git:

vcarlos@C02FL3RLMD6R AI_Learning % git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	curl.py
	curl.sh
	key_dont_push

nothing added to commit but untracked files present (use "git add" to track)
vcarlos@C02FL3RLMD6R AI_Learning % git add curl.py curl.sh
vcarlos@C02FL3RLMD6R AI_Learning % git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   curl.py
	new file:   curl.sh

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	key_dont_push

vcarlos@C02FL3RLMD6R AI_Learning % git commit -m "Added curl files as examples"
[main 2bd89f1] Added curl files as examples
 2 files changed, 70 insertions(+)
 create mode 100644 curl.py
 create mode 100755 curl.sh

# This pushes from origin to main. Could also push to anoher branch using "git push origin <branch_name>

vcarlos@C02FL3RLMD6R AI_Learning % git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.45 KiB | 1.45 MiB/s, done.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:valenciakarlos/AI_Learning.git
   10e3bc6..2bd89f1  main -> main

Using gh to create a pull request:

Create a Pull Request (using gh pr create):

This is where gh comes in. To create a pull request from your branch, use the gh pr create command:


gh pr create



IGNORE_WHEN_COPYING_START
Use code with caution.Bash
IGNORE_WHEN_COPYING_END

This will typically open your default text editor, allowing you to provide a title and a more detailed description for your pull request. gh will automatically populate the base branch (usually main) and the head branch (your branch).

Customizing the Pull Request:

You can customize the pull request creation with flags:

    -t, --title <string>: Specify the pull request title directly from the command line.

    -b, --body <string>: Specify the pull request body directly from the command line.

    --base <branch>: Specify the base branch (the branch you want to merge into). If you don't specify it, it defaults to the default branch of the repository (usually main).

    -d, --draft: Create the pull request as a draft.

Example:


gh pr create -t "Add new feature" -b "This pull request adds the new feature X." --base main


