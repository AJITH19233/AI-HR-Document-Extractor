import { createTheme } from "@mui/material/styles";

const theme = createTheme({

    palette: {

        primary: {
            main: "#2563EB",
        },

        secondary: {
            main: "#3B82F6",
        },

        success: {
            main: "#22C55E",
        },

        warning: {
            main: "#F59E0B",
        },

        error: {
            main: "#EF4444",
        },

        background: {
            default: "#F8FAFC",
            paper: "#FFFFFF",
        },

    },

    typography: {

        fontFamily: [
            "Inter",
            "Segoe UI",
            "Roboto",
            "Arial",
            "sans-serif",
        ].join(","),

        h4: {
            fontWeight: 700,
        },

        h5: {
            fontWeight: 700,
        },

        h6: {
            fontWeight: 600,
        },

        button: {
            textTransform: "none",
            fontWeight: 600,
        }

    },

    shape: {

        borderRadius: 18,

    },

    shadows: [

        "none",

        ...Array(24).fill("0px 10px 25px rgba(15,23,42,0.08)")

    ],

    components: {

        MuiCard: {

            styleOverrides: {

                root: {

                    borderRadius: 20,

                    transition: "all .3s ease",

                    boxShadow: "0 10px 30px rgba(15,23,42,.08)",

                    "&:hover": {

                        transform: "translateY(-6px)",

                        boxShadow: "0 18px 40px rgba(15,23,42,.12)"

                    }

                }

            }

        },

        MuiPaper: {

            styleOverrides: {

                root: {

                    borderRadius: 20

                }

            }

        },

        MuiButton: {

            styleOverrides: {

                root: {

                    borderRadius: 12

                }

            }

        }

    }

});

export default theme;