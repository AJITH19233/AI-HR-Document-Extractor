import api from "../api/api";

export const getDocuments = (page = 1, size = 10, sort = "uploaded_at") =>
    api.get("/documents", {
        params: {
            page,
            size,
            sort
        }
    });

export const getDocument = (id) =>
    api.get(`/documents/${id}`);

export const deleteDocument = (id) =>
    api.delete(`/documents/${id}`);

export const searchDocuments = (query) =>
    api.get("/documents/search", {
        params: {
            query
        }
    });

export const filterDocuments = (params) =>
    api.get("/documents/filter", {
        params
    });

export const getDashboardStats = () =>
    api.get("/documents/stats");