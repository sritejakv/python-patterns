args=("$@")
while read line; do
  # shellcheck disable=SC2006
  filename=`basename "${line}"`
  filename=${filename/py/dot}
  pycallgraph graphviz --dot-file "dynamicCGs/${filename}" -- "${line}"
done < "${args[0]}"
