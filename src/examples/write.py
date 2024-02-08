from h5hist.h5hist import *
import boost_histogram as bh



h = bh.Histogram(bh.axis.Regular(100, -3, 3))
h.fill([0.1, 0.2, 0.3])
h5writehist("foo.h5", "some/path/to/myhist", h)
