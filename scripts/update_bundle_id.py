import os

# Existing bundle ID to be replaced
original_bundle_id = "com.demo.app"

# Desired bundle ID to generate APK for
new_bundle_id = "com.example.app"

# Existing app name to be replaced
original_app_name = "MyApp"

# Desired app name
new_app_name = "MyNewAppName"


# Replace occurrences of original bundle ID
os.system(f"sed -i 's/{original_bundle_id}/{new_bundle_id}/g' android/app/build.gradle")
os.system(f"sed -i 's/{original_bundle_id}/{new_bundle_id}/g' android/app/src/main/java/com/changeid/MainActivity.kt")
os.system(f"sed -i 's/{original_bundle_id}/{new_bundle_id}/g' android/app/src/main/java/com/changeid/MainApplication.kt")

    # Replace occurrences of original app name
os.system(f"sed -i 's/{original_app_name}/{new_app_name}/g' android/app/src/main/res/values/strings.xml")

print(f"Build ID and app name updated successfully! Generated APK for:")
print(f"\t- {new_bundle_id} ({new_app_name})")