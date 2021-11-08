package parser

func Wordizer(text string) []string {
	words := []string{}
	word := []rune{}
	in_string := false
	for _, v := range text {
		if v == ' ' && !in_string {
			words = append(words, string(word))
			word = []rune{}
		} else if v == '"' {
			if in_string {
				in_string = false
				word = append(word, '"')
				// words = append(words, string(word))
				// word = []rune{}
			} else {
				in_string = true
				word = append(word, '"')
			}
		} else {
			word = append(word, v)
		}
	}
	words = append(words, string(word))
	return words
}
