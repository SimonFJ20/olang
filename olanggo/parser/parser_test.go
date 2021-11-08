package parser

import "testing"

func TestParse(t *testing.T) {

	tables := []struct {
		input  string
		output []Operation
	}{
		// {"1", []Operation{{PUSH_INT, 1}}},
		// {"0", []Operation{{PUSH_INT, 0}}},
		// {"-1", []Operation{{PUSH_INT, -1}}},
		// {"34", []Operation{{PUSH_INT, 34}}},
	}

	for _, table := range tables {
		ops := Parse(table.input)
		if len(ops) != len(table.output) {
			t.Errorf("Length does not match")
			continue
		}
		for i, v := range ops {
			if v.Type != table.output[i].Type {
				t.Errorf("OpType does not match")
				break
			}
			if v.Value != table.output[i].Value {
				t.Errorf("Value does not match")
				break
			}
		}
	}

}
