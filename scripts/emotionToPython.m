folder = '/home/aneesh/UbuntuStorage/Homework/MMT/SonusTexere/sorcStone/segmented_audio/';
audio_files = dir(folder);

disp 'abc'

for i = 1:numel(audio_files)
    if audio_files(i).isdir
        continue;
    end
    
    song_name = audio_files(i).name;
    song = load(fullfile(folder, audio_files(i).name));
    song_emotion = song.song_emotion;
    
    vad = get(song_emotion, 'DimData');
    vad = cell2mat(vad{1});
    
    emotions = get(song_emotion, 'ClassData');
    emotions = cell2mat(emotions{1});
    
    out = struct;
    out.vad = vad;
    out.emotions = emotions;
    
    saveFileName = ['/home/aneesh/UbuntuStorage/Homework/MMT/SonusTexere/sorcStone/pythonReady/', erase(song_name, '.mat'), '.mat'];
    save(saveFileName, 'out');
    
end