import os

# Existing ID to be replaced
original_id = "com.changeid"

# Desired build ID to generate APK for
build_ids = "com.changeid.app"

# Replace occurrences of original ID with the new build ID
os.system(f"sed -i 's/{original_id}/{build_ids}/g' android/app/build.gradle")
os.system(f"sed -i 's/{original_id}/{build_ids}/g' android/app/src/main/java/com/changeid/MainActivity.kt")
os.system(f"sed -i 's/{original_id}/{build_ids}/g' android/app/src/main/java/com/changeid/MainApplication.kt")

print(f"Build ID updated successfully! Generated APK for:")
print(f"\t- {build_ids}")

