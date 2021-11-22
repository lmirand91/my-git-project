 #     git init                             //initializes repository
 #     git status                           //shows current state of repository
 #     dir                                  //shows all available files in directory (doesn't include hidden unless change setting)
 #     git add .                            //updates repository with all untracked files, as well as changed files
 #     git add my_file.py                   //updates respository with specific file by including path to file
 #     git rm --cached my_file.py           //removed cached file from queue
 #     git commit -m "Initial commit"       //m for message, commits file to git repository (creates a version)
 #     git remote add origin https://github.com/lmirand91/my-git-project.git 
 #     //connects github (remote) repository to local repository --origin-represents named remote
 #     git remote -v                        //lets you view the named origin with fetch and push shown
 #     git branch -M main                   //specifies main branch
 #     git push -u origin main              //pushes to remote repository
 #     git log                              //shows all previous activity of repository
 #     git branch                           //shows what branch we are on
 #     git checkout -b readme-styling       //readme-styling is an example, switches to new branch
 #     git checkout main                    //switch back to main branch
 #     git merge readme-styling             //merges feature branch with main
 #     git push -u origin another-feature   //u stands for upstream, pushing branch to github
 #     git rebase master                    //rebases feature branch to reflect changes from main branch 

 #  Following commands are git commands, that aren't specific to github
 #  On github, new repository, needs a name unique to your set of repositories
 #  Branches - ability to have connection to working application while working on a project off to the side without affecting the working product
 # Never ever perform a rebase on a shared feature branch
 # 