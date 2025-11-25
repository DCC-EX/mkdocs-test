# Print lines that start with optional whitespace followed by "#define"
# Usage: awk -f pull-exrail.awk inputfile > outputfile
/^[[:space:]]*#define/ {
    line = $0
    sub(/^[[:space:]]*#define[[:space:]]*/ , "" , line)
    print "\n```cpp\n" line "\n```\n"
    next
}



# Match lines starting with optional space then "///brief" and remove the prefix
/^[[:space:]]*\/\/\/brief/ {
    line = $0
    sub(/^[[:space:]]*\/\/\/brief[[:space:]]*/ , "" , line)
    print line
    print ""
    next
}
# Match lines starting with optional space then "///param" and remove the prefix
/^[[:space:]]*\/\/\/param/ {
    line = $0
    sub(/^[[:space:]]*\/\/\/param[[:space:]]*/ , "- " , line)
    print line
    next
}


# Copy any other lines starting with "///" removing the "///" prefix
/^[[:space:]]*\/\/\// {
    line = $0
    sub(/^[[:space:]]*\/\/\/[[:space:]]*/ , "" , line)
    print line
    print ""
    next
}


