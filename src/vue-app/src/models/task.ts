export interface Task {
    id: number | null;
    user_id: string;
    name: string;
    tags: string[] | null;
    comments: string | null;
    state: string;
    deadline: string | null;

}