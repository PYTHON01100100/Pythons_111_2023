import os
import subprocess

# دالة للحصول على قائمة المجلدات داخل المجلد الرئيسي
def list_folders(base_folder_path):
    try:
        # قم بإنشاء قائمة بجميع المجلدات داخل المسار المحدد
        folders = [f for f in os.listdir(base_folder_path) if os.path.isdir(os.path.join(base_folder_path, f))]
        folders.sort()
        return folders
    except Exception as e:
        print(f"Error: {e}")
        return []

# دالة للحصول على قائمة الحلقات داخل مجلد الأنمي
def list_episodes(folder_path):
    try:
        # قم بإنشاء قائمة بجميع الملفات داخل المسار المحدد
        episodes = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        episodes.sort()
        return episodes
    except Exception as e:
        print(f"Error: {e}")
        return []

# دالة لتشغيل حلقة معينة
def play_episode(folder_path, episode):
    episode_path = os.path.join(folder_path, episode)
    try:
        # استبدل 'C:\\Program Files\\VideoLAN\\VLC\\vlc.exe' بالمسار إلى مشغل الفيديو الخاص بك
        subprocess.run(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe', episode_path])  
    except Exception as e:
        print(f"Error: {e}")

# الدالة الرئيسية لتشغيل البرنامج
def main():
    base_folder_path = 'C:\\Users\\d7oom\\Videos\\تكملة'  # المسار الرئيسي لمجلد الأنميات
    if not os.path.isdir(base_folder_path):
        print("Invalid folder path.")  # تحقق من صحة المسار
        return

    folders = list_folders(base_folder_path)
    if not folders:
        print("No folders found in the specified folder.")  # تحقق من وجود مجلدات
        return

    print("\nAvailable anime series:")
    for idx, folder in enumerate(folders):
        print(f"{idx + 1}. {folder}")  # عرض قائمة الأنميات المتاحة

    try:
        folder_choice = int(input("\nEnter the number of the anime series to view its episodes: "))
        if 1 <= folder_choice <= len(folders):
            selected_folder = folders[folder_choice - 1]
            selected_folder_path = os.path.join(base_folder_path, selected_folder)

            episodes = list_episodes(selected_folder_path)
            if not episodes:
                print("No episodes found in the selected folder.")  # تحقق من وجود حلقات
                return

            print(f"\nAvailable episodes for {selected_folder}:")
            for idx, episode in enumerate(episodes):
                print(f"{idx + 1}. {episode}")  # عرض قائمة الحلقات المتاحة

            while True:
                try:
                    episode_choice = int(input("\nEnter the number of the episode to play (or 0 to exit): "))
                    if episode_choice == 0:
                        break  # خروج من البرنامج
                    elif 1 <= episode_choice <= len(episodes):
                        play_episode(selected_folder_path, episodes[episode_choice - 1])
                    else:
                        print("Invalid choice. Please enter a number from the list.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            print("Invalid choice. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()


"""

شرح الكود بالعربية:
استيراد المكتبات المطلوبة:

os: للوصول إلى نظام الملفات.
subprocess: لتشغيل أوامر النظام.
دالة list_folders:

تعود بقائمة المجلدات الموجودة داخل مجلد معين.
دالة list_episodes:

تعود بقائمة الملفات (الحلقات) الموجودة داخل مجلد معين.
دالة play_episode:

تشغل حلقة معينة باستخدام مشغل الفيديو الافتراضي.
الدالة الرئيسية main:

تحدد المسار الرئيسي لمجلد الأنميات.
تعرض قائمة الأنميات المتاحة.
تعرض قائمة الحلقات المتاحة للأنمي المختار.
تسمح للمستخدم بتشغيل حلقة معينة أو الخروج من البرنامج.
Explanation in English:
Import Required Libraries:

os: To interact with the file system.
subprocess: To run system commands.
Function list_folders:

Returns a list of folders inside a specified directory.
Function list_episodes:

Returns a list of files (episodes) inside a specified folder.
Function play_episode:

Plays a specified episode using the default video player.
Main Function main:

Sets the main path for the anime folder.
Displays the available anime series.
Displays the available episodes for the selected anime.
Allows the user to play a specific episode or exit the program.






"""