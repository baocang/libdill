
fxs.append(
    {
        "name": "ipaddr_remotes",
        "topic": "IP addresses",
        "info": "resolve the address of a remote IP endpoint",
        "result": {
            "type": "int",
            "success": "number of IP addresses returned",
            "error": "-1",
        },
        "args": [
            {
                "name": "addrs",
                "type": "struct ipaddr*",
                "dill": True,
                "info": "Out parameter. Array of resulting IP addresses.",
            },
            {
                "name": "naddrs",
                "type": "int",
                "info": "Size of **addrs** array.",
            },
            {
                "name": "name",
                "type": "const char*",
                "info": "Name of the remote IP endpoint, such as \"www.example.org\" or \"192.168.0.111\".",
            },
            {
                "name": "port",
                "type": "int",
                "info": "Port number. Valid values are 1-65535.",
            },
            {
                "name": "opts",
                "type": "const struct ipaddr_opts*",
                "dill": True,
                "info": "Options.",
            },
        ],

        "has_deadline": True,

        "prologue": """
            Converts an IP address in human-readable format, or a name of a
            remote host into an array of **ipaddr** structures. If there's no
            associated address, the function succeeds and returns zero.
        """ + "\n\n" + ipaddr_mode,


        "example": ipaddr_example,
    }
)
