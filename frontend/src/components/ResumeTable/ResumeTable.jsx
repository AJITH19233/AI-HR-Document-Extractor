import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Chip,
  IconButton,
  Link,
  Tooltip,
} from "@mui/material";
import { Avatar } from "@mui/material";
import VisibilityIcon from "@mui/icons-material/Visibility";
import DeleteIcon from "@mui/icons-material/Delete";
import DescriptionIcon from "@mui/icons-material/Description";

function getScoreColor(score) {
  if (score >= 80) return "success";
  if (score >= 60) return "warning";
  return "error";
}

function ResumeTable({ documents }) {
  return (
    <TableContainer
      component={Paper}
      elevation={3}
      sx={{
        mt: 4,
        borderRadius: 3,
      }}
    >
      <Table>

        <TableHead
    sx={{
        backgroundColor:"#EFF6FF"
    }}
>
          <TableRow>

            <TableCell><b>Name</b></TableCell>

            <TableCell><b>Email</b></TableCell>

            <TableCell><b>Resume</b></TableCell>

            <TableCell align="center"><b>Score</b></TableCell>

            <TableCell align="center"><b>Status</b></TableCell>

            <TableCell align="center"><b>Uploaded</b></TableCell>

            <TableCell align="center"><b>Actions</b></TableCell>

          </TableRow>
        </TableHead>

        <TableBody>

          {documents.map((doc) => (

            <TableRow
    key={doc.id}
    hover
    sx={{
        transition:".25s",

        "&:hover":{

            background:"#F8FAFC",

            transform:"scale(1.002)"

        }

    }}
>

              <TableCell>

    <div
        style={{
            display:"flex",
            alignItems:"center",
            gap:"12px"
        }}
    >

        <Avatar
            sx={{
                bgcolor:"#2563EB",
                width:38,
                height:38
            }}
        >
            {doc.name.charAt(0)}
        </Avatar>

        <div>

            <strong>{doc.name}</strong>

            <br/>

            <span
                style={{
                    color:"#64748B",
                    fontSize:13
                }}
            >
                Candidate
            </span>

        </div>

    </div>

</TableCell>

              <TableCell>
                {doc.email}
              </TableCell>

              <TableCell>

            <div
    style={{
        display:"flex",
        alignItems:"center",
        gap:"8px"
    }}
>

    <DescriptionIcon
        color="primary"
        fontSize="small"
    />

    <Link
        href="#"
        underline="hover"
    >
        {doc.original_filename}
    </Link>

</div>

              </TableCell>

              <TableCell align="center">

                <Chip
                  label={doc.resume_score}
                  color={getScoreColor(doc.resume_score)}
                  size="small"
                />

              </TableCell>

              <TableCell align="center">

                <Chip
                  label={doc.status}
                  color="success"
                  size="small"
                />

              </TableCell>

              <TableCell align="center">

                {new Date(doc.uploaded_at).toLocaleDateString()}

              </TableCell>

              <TableCell align="center">

                <Tooltip title="View Resume">

                  <IconButton color="primary">

                    <VisibilityIcon />

                  </IconButton>

                </Tooltip>

                <Tooltip title="Delete Resume">

                  <IconButton color="error">

                    <DeleteIcon />

                  </IconButton>

                </Tooltip>

              </TableCell>

            </TableRow>

          ))}

        </TableBody>

      </Table>
    </TableContainer>
  );
}

export default ResumeTable;