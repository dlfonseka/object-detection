
# Tensorflow Object Detection API

This is fork of the Tensorflow Object Detection API from the `research/object_detection` subdirectory of the upstream repository [tensorflow/models](https://github.com/tensorflow/models). This branch, object-detection-v2, contains the Tensorflow 2.2 version, released on July 10th, 2020. The object-detection branch contains the legacy Tensorflow 1.14 version from an earlier commit.

To install: `pip install https://github.com/autognc/object-detection/tarball/object-detection-v2`

## Syncing upstream changes

In order to maintain a fork of only a subdirectory of an upstream repository, `git subtree split` was used. Unfortunately, this also means that merging in upstream changes is a bit more involved. Here are the steps for syncing the fork:

```
# clone and enter this repo
git clone https://github.com/autognc/object-detection
cd object-detection

# fetch the upstream repo
git remote add upstream https://github.com/tensorflow/models
git fetch upstream

# checkout upstream changes
git checkout upstream/master
git checkout <commit hash> # OPTIONAL: only if you don't want the most recent version

# split the subtree into a new branch (this may take awhile)
git subtree split --prefix research/object_detection -b tmp

# merge the changes
git checkout object-detection-v2
git merge tmp

# clean up
git branch -D tmp

# push changes
git push origin object-detection-v2
```

You might notice that this repo also has another branch, `slim-v2`. That is because the object detection API depends on another subdirectory of the upstream repository, `research/slim`. If you update the object detection branch, then you should probably also update the slim branch to maintain compatibility:

```
git checkout upstream/master
git checkout <commit hash> # again optional, if you did do this above, you should probably use the same commit hash
git subtree split --prefix research/slim -b tmp
git checkout slim-v2
git merge tmp
git branch -D tmp
git push origin slim-v2
```
