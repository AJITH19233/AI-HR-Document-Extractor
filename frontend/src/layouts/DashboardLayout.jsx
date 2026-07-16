import { Box } from "@mui/material";

import Sidebar from "../components/Sidebar/Sidebar";
import Navbar from "../components/Navbar/Navbar";

function DashboardLayout({ children }) {

    return (

        <Box
            sx={{
                display:"flex"
            }}
        >

            <Sidebar/>

            <Box
                sx={{
                    ml:"280px",
                    width:"calc(100% - 280px)",
                    background:
                    "linear-gradient(135deg,#F8FAFC,#EEF4FF)",
                    minHeight:"100vh"
                }}
            >

                <Navbar/>

                <Box
                    sx={{
                        p:4
                    }}
                >

                    {children}

                </Box>

            </Box>

        </Box>

    );

}

export default DashboardLayout;