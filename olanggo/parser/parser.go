package parser

type OpType int

const (
	PUSH_INT = iota
)

type Operation struct {
	Type  OpType
	Value int
}

func Parse(program string) []Operation {
	ops := []Operation{}
	// for i, v := range program {

	// 	numre := regexp.MustCompile("^\\-?\\d+$")
	// 	if numre.MatchString(v)
	// }
	return ops
}
