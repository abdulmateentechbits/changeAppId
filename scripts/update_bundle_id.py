# -------------------------------------------------------------------------------
# SCRIPT PURPOSE AND USAGE
# -------------------------------------------------------------------------------

# This script is designed to streamline the process of managing various app settings
# for Android applications.

# It currently supports the following actions:
#   - Changing the app label name
#   - Updating the bundle ID

# To use the script:
#   1. Ensure you have Python3 installed on your system.
#   2. Verify that you have python by running the command on terminal python3 --version
#   3. Run the chmod +x scripts/update_bundle_id.py
#   4. python3 scripts/update_bundle_id.py
#   5. clean your project and rebuild it.
#   6. Generate your apk
#   7. If you have face any issue comment below the video i will reply you: https://youtu.be/iT-mu06MyKI


import os

# BUNDLE ID
# -----------------------------------------------

# Existing bundle ID to be replaced
original_bundle_id = "com.example.app"

# Desired bundle ID to generate APK for
new_bundle_id = "com.example.new.app"

# -----------------------------------------------

# APP LABEL NAME

# +++++++++++++++++++++++++++++++++++++++++++++++

# Default app label name: ResERP (Remain unchanged)

# Existing app name to be replaced
original_app_name = "Helloworld"

# Desired app nameyarn 
new_app_name = "Helloworld2"

# +++++++++++++++++++++++++++++++++++++++++++++++++++


# Replace occurrences of original bundle ID
os.system(f"sed -i 's/{original_bundle_id}/{new_bundle_id}/g' android/app/build.gradle")
os.system(f"sed -i 's/{original_bundle_id}/{new_bundle_id}/g' android/app/src/main/java/com/myreserp/paragon/fm/app/MainActivity.java")
os.system(f"sed -i 's/{original_bundle_id}/{new_bundle_id}/g' android/app/src/main/java/com/myreserp/paragon/fm/app/MainApplication.java")

# Replace occurrences of original app name
os.system(f"sed -i 's/{original_app_name}/{new_app_name}/g' android/app/src/main/res/values/strings.xml")

print(f"Build ID and app name updated successfully! Generated APK for:")
print(f"\t- {new_bundle_id} ({new_app_name})")
