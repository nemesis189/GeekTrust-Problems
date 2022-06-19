def run_commands(commands, stream_app):
    command_name_index = 0
    command_A_index = 1
    command_B_index = 2

    for cmd in commands:
        if cmd[command_name_index] == 'START_SUBSCRIPTION':
            stream_app.set_start_date(cmd[command_A_index])

        elif cmd[command_name_index] == 'ADD_SUBSCRIPTION':
            stream_app.add_subscription(cmd[command_A_index], cmd[command_B_index])

        elif cmd[command_name_index] == 'ADD_TOPUP':
            stream_app.add_topup(cmd[1], cmd[command_B_index])

        elif cmd[command_name_index] == 'PRINT_RENEWAL_DETAILS':
            stream_app.print_renewal_details()