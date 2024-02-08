import h5py
import boost_histogram

def h5writehist(filename, path, h):
    with h5py.File(filename, "w") as f:
        g = f.create_group(path)
        g.create_dataset("weights", data=h.view())
        g.create_dataset("sumw2", data=h.variances())
        for dim, edges in enumerate(h.axes):
            g.create_dataset(f"edges_{dim}", data=edges.edges)
        g.attrs["overflow"] = h
        g.attrs["nentries"] = h.
        g.attrs["_producer"] = "h5hist.py"
        g.attrs["_h5hist_version"] = str(CURRENT_H5HIST_VERSION)
