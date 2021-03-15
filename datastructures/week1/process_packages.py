# python3

"""
buffer size, number of packets coming
time it comes, time needed to process
time it comes, time needed to process..
time it comes, time needed to process....
"""

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.end_time = []

    def delete_processed(self, request):
        """deletes processed elements of the buffer by the request's arrival time."""
        while self.end_time:
            if self.end_time[0] <= request.arrived_at:
                self.end_time.pop(0)
            else:
                break

    def process(self, request):
        """Processes incoming request."""
        self.delete_processed(request)

        if len(self.end_time) == self.size:  # if buffer is full
            return Response(True, -1)

        if len(self.end_time) == 0:  # if buffer is empty
            self.end_time = [request.arrived_at + request.time_to_process]
            return Response(False, request.arrived_at)

        # print the previously last element that was added since there is still space
        # in the buffer to store
        response = Response(False, self.end_time[-1])
        # change the last element to the current request
        self.end_time.append(self.end_time[-1] + request.time_to_process)
        return response


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
