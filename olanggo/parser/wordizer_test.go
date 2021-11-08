package parser

import "testing"

func TestWordizer(t *testing.T) {

	tables := []struct {
		input  string
		output []string
	}{
		{"test", []string{"test"}},
		{"dup swap", []string{"dup", "swap"}},
		{"1 -1", []string{"1", "-1"}},
		{"\"hello world\"", []string{"\"hello world\""}},
		{"\"hello world\" print_str", []string{"\"hello world\"", "print_str"}},
	}

	for _, table := range tables {
		res := Wordizer(table.input)
		if len(res) != len(table.output) {
			t.Errorf("Length does not match")
		}
		for i, v := range res {
			if v != table.output[i] {
				t.Log(v, table.output[i])
				t.Errorf("Word does not match")
				break
			}
		}
	}

}
