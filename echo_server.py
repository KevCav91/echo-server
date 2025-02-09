import socket
import sys
import traceback


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)

    with socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM,
                       socket.IPPROTO_TCP) as sock:

        # log that we are building a server
        print("making a server on {0}:{1}".format(*address), file=log_buffer)

        sock.bind(address)
        sock.listen(1)

        try:
            # the outer loop controls the creation of new connection sockets.
            # The server will handle each incoming connection one at a time.
            while True:
                print('waiting for a connection', file=log_buffer)
                conn, addr = sock.accept()
                try:
                    print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                    # the inner loop will receive messages sent by the client in
                    # buffers.  When a complete message has been received, the
                    # loop will exit
                    while True:
                        data = conn.recv(16)
                        print('received "{0}"'.format(data.decode('utf8')))

                        conn.sendall(data)

                        # the fact using the print statement here.
                        # It will help in debugging problems.

                        print('sent "{0}"'.format(data.decode('utf8')))

                        # of the message. If you have, then break from the
                        # `while True` loop.

                        # Figuring out whether or not you have received the
                        # end of the message is a trick we learned in the
                        # lesson: if you don't remember then ask your
                        # classmates or instructor for a clue.
                        # :)

                        if len(data) < 16:
                            break

                except Exception as e:
                    traceback.print_exc()
                    sys.exit(1)
                finally:
                    conn.close()
                    print(
                        'echo complete, client connection closed',
                        file=log_buffer)

        except KeyboardInterrupt:
            sock.close()
            print('quitting echo server', file=log_buffer)


if __name__ == '__main__':
    server()
    sys.exit(0)
