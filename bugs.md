- mat file for videvents does not contain correct headers (time)
- json format documentation
- add subtitle data requirement to the readme
- no actors in any dune subtitles we could find

'\n\n[0-9]' to '\n'
'<[a-z\/]*>' to ''

- done till chapter 34 only, this is where the movie ends

- chapterText from bookQuoteExtractor requires double quotes, need to add these to each chapter line
    - mainly problems relate to different movies having different formats of text and subtitles

- fixed error in clip alignment to handle intro chapters that are not in the movie and are thus not assigned corresponding scenes
- had to put voice result in main, pickle loading error