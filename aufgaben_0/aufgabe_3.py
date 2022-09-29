from turtle import forward, left, done


def octagon_spiral(edge_len, step_size):
    while edge_len > 0:
        forward(edge_len)
        left(45)
        edge_len -= step_size

octagon_spiral(100, 2)
done() # prevents turtle drawing window from closing immediately
