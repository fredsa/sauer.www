#!/bin/bash
#
set -ue

PROJECT=sauer-www

if [ $( echo "$*" | egrep -- '-v'\|'--version=' >/dev/null; echo $? ) != 0 ]
then
  cat <<EOD

ERROR: Must specify explict '-v <version>' argument, e.g.

   $0 -v <version>

EOD
  exit 1
fi

echo -e "\n*** DEPLOYING ***\n"
gcloud.cmd app deploy --project $PROJECT --quiet $* app.yaml

echo
echo "Configure default version here:"
echo "  https://console.cloud.google.com/appengine/versions?project=$PROJECT"
