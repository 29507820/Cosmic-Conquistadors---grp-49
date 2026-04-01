=
        GITHUB TERMINOLOGY
=
(for if you're new to this stuff like me)

- Clone: create a copy of the entire repository locally onto YOUR LAPTOP
- Pull: Update Locally Saved Code (the clone) 
- Commit: Save Changes Locally (after changing the code that was "pulled" previously)
- Push: Send Changes to GitHub, updating the shared doc so we can all access and view your changes
- Rollback: Undo Changes and Restore an older version of the shared file, in case someone messes something up

In Powershell: (Assuming you have the repository cloned on your computer and are currently in the folder)
Pull        - git pull
(open the file and make your changes)
(make sure files run before adding them back to repository pls)
Commit      - git checkout main
              git add .
              git commit -m "any comments on what you've changed"
              
Push        - git push
