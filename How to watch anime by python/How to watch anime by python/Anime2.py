import os
import subprocess

# Function to list folders (anime series) in the specified base folder
def list_folders(base_folder_path):
    try:
        folders = [f for f in os.listdir(base_folder_path) if os.path.isdir(os.path.join(base_folder_path, f))]
        folders.sort()
        return folders
    except Exception as e:
        print(f"Error: {e}")
        return []

# Function to list episodes in the selected anime series folder
def list_episodes(folder_path):
    try:
        episodes = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        episodes.sort()
        return episodes
    except Exception as e:
        print(f"Error: {e}")
        return []

# Function to play the selected episode
def play_episode(folder_path, episode):
    episode_path = os.path.join(folder_path, episode)
    try:
        subprocess.run(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe', episode_path])  # Replace with the path to your video player executable
    except Exception as e:
        print(f"Error: {e}")

# Main function to handle user interactions
def main():
    base_folder_path = 'C:\\Users\\d7oom\\Videos\\تكملة'
    if not os.path.isdir(base_folder_path):
        print("Invalid folder path.")
        return

    while True:
        folders = list_folders(base_folder_path)
        if not folders:
            print("No folders found in the specified folder.")
            return

        print("\nAvailable anime series:")
        for idx, folder in enumerate(folders):
            print(f"{idx + 1}. {folder}")

        try:
            folder_choice = int(input("\nEnter the number of the anime series to view its episodes (or 0 to exit): "))
            if folder_choice == 0:
                break
            elif 1 <= folder_choice <= len(folders):
                selected_folder = folders[folder_choice - 1]
                selected_folder_path = os.path.join(base_folder_path, selected_folder)

                while True:
                    episodes = list_episodes(selected_folder_path)
                    if not episodes:
                        print("No episodes found in the selected folder.")
                        break

                    print(f"\nAvailable episodes for {selected_folder}:")
                    for idx, episode in enumerate(episodes):
                        print(f"{idx + 1}. {episode}")

                    try:
                        episode_choice = int(input("\nEnter the number of the episode to play (or 0 to go back): "))
                        if episode_choice == 0:
                            break
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

Explanation in Arabic:
استيراد المكتبات المطلوبة:

os: للوصول إلى نظام الملفات.
subprocess: لتشغيل أوامر النظام.
دالة list_folders:

تعود بقائمة المجلدات (الأنميات) الموجودة داخل المجلد الرئيسي المحدد.
دالة list_episodes:

تعود بقائمة الملفات (الحلقات) الموجودة داخل مجلد الأنمي المحدد.
دالة play_episode:

تشغل الحلقة المحددة باستخدام مشغل الفيديو الافتراضي.
الدالة الرئيسية main:

تحدد المسار الرئيسي لمجلد الأنميات.
تعرض قائمة الأنميات المتاحة.
تسمح للمستخدم باختيار أنمي معين.
تعرض قائمة الحلقات المتاحة للأنمي المختار.
تسمح للمستخدم بتشغيل حلقة معينة أو الرجوع إلى قائمة الأنميات أو الخروج من البرنامج.
Explanation in English:
Import Required Libraries:

os: To interact with the file system.
subprocess: To run system commands.
Function list_folders:

Returns a list of folders (anime series) inside the specified base folder.
Function list_episodes:

Returns a list of files (episodes) inside the specified anime series folder.
Function play_episode:

Plays the specified episode using the default video player.
Main Function main:

Sets the main path for the anime folder.
Displays the available anime series.
Allows the user to select an anime series.
Displays the available episodes for the selected anime series.
Allows the user to play a specific episode, go back to the anime series list, or exit the program.







"""