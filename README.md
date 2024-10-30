### introduction

A simple cli tool for fasta file reading and statistics

### Usage

    Usage: statseq [OPTIONS] COMMAND [ARGS]...

**Commands**
```
- reader
    Fasta Reader Function
- stat
    Fasta Sequence Stat Function
```

#### reader
```
Options 
--filepath  -f      PATH  Input fasta file path. [default: None][required]                                                                   
--attrs     -a      TEXT  Input one or more values, separated by commas [default: id,seq,seq_len,gc_content]                                                                                     
--help      -h            Show this message and exit.  
```

#### stat 
```
Options 
--filepath  -f      PATH  Input fasta file path. [default: None] [required]  
--attrs     -a      TEXT  Input one or more values, separated by commas [default: id,seq,seq_len,gc_content]
--help      -h            Show this message and exit.   
```