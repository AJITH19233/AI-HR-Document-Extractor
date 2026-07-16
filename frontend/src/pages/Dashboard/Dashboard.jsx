import { useEffect, useState } from "react";

import Grid from "@mui/material/Grid";
import DescriptionIcon from "@mui/icons-material/Description";
import StarIcon from "@mui/icons-material/Star";
import EmojiEventsIcon from "@mui/icons-material/EmojiEvents";
import TrendingDownIcon from "@mui/icons-material/TrendingDown";
import DashboardLayout from "../../layouts/DashboardLayout";
import DashboardCard from "../../components/DashboardCard/DashboardCard";
import ResumeTable from "../../components/ResumeTable/ResumeTable";
import DashboardHero from "../../components/DashboardHero/DashboardHero";
import {
  getDashboardStats,
  getDocuments,
} from "../../services/documentService";

function Dashboard() {
  const [stats, setStats] = useState({
    total_resumes: 0,
    average_resume_score: 0,
    highest_resume_score: 0,
    lowest_resume_score: 0,
  });

  const [documents, setDocuments] = useState([]);

  useEffect(() => {
    loadDashboard();
  }, []);

  async function loadDashboard() {
    try {
      const statsResponse = await getDashboardStats();
      setStats(statsResponse.data);

      const documentResponse = await getDocuments();
      setDocuments(documentResponse.data);
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <DashboardLayout>
        <DashboardHero />

<Grid
    container
    spacing={4}
></Grid>
      <Grid container spacing={3}>
        <Grid size={{ xs: 12, md: 3 }}>
          <DashboardCard
            title="Total Resumes"
            value={stats.total_resumes}
            icon={<DescriptionIcon/>}
            color="#2563EB"
            />
        </Grid>

        <Grid size={{ xs: 12, md: 3 }}>
          <DashboardCard
        title="Average Score"
        value={stats.average_resume_score}
        icon={<StarIcon/>}
        color="#22C55E"

/>
        </Grid>

        <Grid size={{ xs: 12, md: 3 }}>
          <DashboardCard
            title="Highest Score"
            value={stats.highest_resume_score}
            icon={<EmojiEventsIcon/>}
            color="#F59E0B"
/>
        </Grid>

        <Grid size={{ xs: 12, md: 3 }}>
          <DashboardCard
            title="Lowest Score"
            value={stats.lowest_resume_score}
            icon={<TrendingDownIcon/>}
            color="#EF4444"
/>
        </Grid>
      </Grid>

      <ResumeTable documents={documents} />
    </DashboardLayout>
  );
}

export default Dashboard;